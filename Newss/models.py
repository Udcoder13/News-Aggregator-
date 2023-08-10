from django.db import models

# Create your models here.
class News(models.Model):
     title = models.CharField(max_length=50)
     description = models.TextField()
     content=models.TextField(blank=True)
     url=models.URLField(blank=True)
     image = models.ImageField(upload_to='static/images/')
     publishedAt = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self) :
          return self.title
      