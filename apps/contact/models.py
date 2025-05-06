from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    update_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name