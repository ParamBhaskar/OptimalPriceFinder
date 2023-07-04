from django.db import models

# Create your models here.


class Product(models.Model):
    # unique_id=models.CharField(max_length=5000,null=True)
    name = models.TextField(blank=True)
    # image=models.ImageField()
    price = models.CharField(max_length=50)
    stars = models.TextField(blank=True)
    # feature_bullets=models.TextField()
    rating_count = models.TextField(blank=True)
    # variant_data=models.TextField()
    availability = models.TextField(blank=True)
    product_url = models.URLField(blank=True)
    onlineStore = models.TextField(blank=True)

    def __str__(self):
        return self.name + " ["+str(self.price)+']' + " ["+str(self.onlineStore)+']'


class contacted_user(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name + " ["+str(self.email)+']' + " ["+str(self.message)+']'
