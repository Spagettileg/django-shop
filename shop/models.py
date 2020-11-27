from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=2, blank=True, null=True)
    
    def __str__(self):
        return self.name