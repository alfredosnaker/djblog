from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    #auth.User es un modelo de django que implementa un usuario dentro de la base de datos
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(blank=True,null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
            
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        