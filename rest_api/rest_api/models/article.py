# myapp/models.py
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)   
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()  
    published = models.BooleanField()
    images = models.ImageField(upload_to='images/',blank=True,null=True)

    
    def __str__(self):
        return self.title
