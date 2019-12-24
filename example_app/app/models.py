from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
