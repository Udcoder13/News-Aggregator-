from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class News(models.Model):
     title = models.CharField(max_length=50)
     description = models.TextField(null=True, blank=True)
     content=models.TextField(null=True, blank=True)
     url=models.URLField(blank=True)
     image = models.ImageField(upload_to='static/images/')
     publishedAt = models.DateTimeField(auto_now_add=True)
     source=models.CharField(max_length=50,blank=True)
     
     
     def __str__(self) :
          return self.title

class comments(models.Model):
      comments = models.TextField(null=True, blank=True,max_length=200)
      user= models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
      news=models.ForeignKey(News,null=True,on_delete=models.CASCADE,related_name='comments')
      article_url = models.URLField(null=True)  # Add this field to store the article's URL
