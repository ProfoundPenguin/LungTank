from django.db import models
from django.utils.translation import gettext_lazy as _  # Import this
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

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
    image = models.ImageField(upload_to="product_images")

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f"Image for {self.product.name}"


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