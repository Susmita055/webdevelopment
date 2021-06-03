from django.conf import settings
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)




    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField(max_length=1000) 
    created_on =models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment {} by {}'.format(self.body,self.name)


#added for subscribe
class form(models.Model):
    email= models.EmailField()
    name=models.CharField(max_length=30)
