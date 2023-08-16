from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return f'products/{self.id}'
    