from django.db import models
import uuid

def _generate_upload_path(instance, filename):
    return f'products/{instance.uuid}/{filename}'

class Product(models.Model):
    # Fields
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=_generate_upload_path)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=12, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    
    # Methods
    def __str__(self) -> str:
        return self.name
