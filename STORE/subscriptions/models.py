from django.db import models

# Create your models here.

class subscriptions(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.name
