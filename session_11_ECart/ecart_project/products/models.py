from django.db import models

# Create your models here.

class ProductAll(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)  # For external URLs
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name + " " + str(self.product_price)
    
    def get_image_url(self):
        """Return image URL - either from uploaded file or external URL"""
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return None
    