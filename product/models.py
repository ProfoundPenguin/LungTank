from django.db import models
from django.utils.translation import gettext_lazy as _  # Import this
from django.core.validators import RegexValidator
from django.core.files.base import ContentFile
from django.utils.translation import gettext_lazy as _
from PIL import Image as PilImage
import io
from django.dispatch import receiver
from django.db.models.signals import post_save

class Product(models.Model):
    name = models.TextField(max_length=120, null=False, blank=False)
    slug = models.SlugField(
        max_length=120, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-z0-9-]+$',
                message='Slug can only contain lowercase letters, numbers, and hyphens.'
            )
        ]
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    dis_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower().replace(" ", "-")  # Ensure lowercase and replace spaces with hyphens
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class Product_Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to="product_images/original/")
    image_400 = models.ImageField(upload_to="product_images/400/", null=True, blank=True)
    image_700 = models.ImageField(upload_to="product_images/700/", null=True, blank=True)
    image_2000 = models.ImageField(upload_to="product_images/2000/", null=True, blank=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f"Image for {self.product.name}"

    def save(self, *args, **kwargs):
        # Create WebP images on save
        if self.original_image:
            self.convert_to_webp()
        super().save(*args, **kwargs)

    def convert_to_webp(self):
        # Open the original image
        img = PilImage.open(self.original_image)
        
        # Create a bytes buffer for the WebP images
        webp_buffer_400 = io.BytesIO()
        webp_buffer_700 = io.BytesIO()
        webp_buffer_2000 = io.BytesIO()

        # Generate and save different sizes
        for size, buffer in [(400, webp_buffer_400), (700, webp_buffer_700), (2000, webp_buffer_2000)]:
            img_copy = img.copy()
            if size < img_copy.width:
                img_copy.thumbnail((size, size))

            # Save the image in WebP format to the buffer
            img_copy.save(buffer, format='WEBP')
            buffer.seek(0)

            # Save to the corresponding field
            file_name = f"{self.product.id}_{size}.webp"
            content_file = ContentFile(buffer.read(), name=file_name)

            if size == 400:
                self.image_400.save(file_name, content_file, save=False)
            elif size == 700:
                self.image_700.save(file_name, content_file, save=False)
            elif size == 2000:
                self.image_2000.save(file_name, content_file, save=False)

@receiver(post_save, sender=Product_Image)
def create_webp_images(sender, instance, created, **kwargs):
    if created:
        instance.convert_to_webp()


class Sale(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('completed', _('Completed')),
        ('shipped', _('Shipped')),
        ('canceled', _('Canceled')),
    ]

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="sales")
    quantity = models.PositiveIntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)  # Stores price of product at time of sale
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Calculated total (price * quantity)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Stripe related fields
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', _('Pending')),
        ('paid', _('Paid')),
        ('failed', _('Failed')),
    ], default='pending')

    date_added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")
        ordering = ['-date_added']

    def __str__(self):
        return f"Sale of {self.product.name} (x{self.quantity})"