from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

User = get_user_model()


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    info = models.CharField(max_length=20)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male',),
        ('female', 'Female',),
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-date_added',)
    def __str__(self):
        return self.name