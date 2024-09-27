from django.contrib import admin
from . import models
from view import models as view_model

# Register your models here.
admin.site.register(models.Product)
class ProductImageAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin
    fields = ('product', 'original_image')
    list_display = ('product', 'original_image')  # Fields to display in the list view

# Register the model with the custom admin class
admin.site.register(models.Product_Image, ProductImageAdmin)
admin.site.register(models.Sale)
admin.site.register(view_model.Faq)
