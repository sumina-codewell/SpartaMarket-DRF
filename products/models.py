from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='product_images/')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="accounts"
    )

    def __str__(self):
        return self.title