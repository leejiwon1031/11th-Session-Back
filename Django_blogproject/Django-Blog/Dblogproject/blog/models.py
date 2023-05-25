from django.db import models
from django.utils import timezone

class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()
    hashtag=models.ManyToManyField(HashTag)
    photo=models.ImageField(blank=True, null=True, upload_to="blog_photo")

    def __str__(self):
        return self.title
    
    #Blog 클래스 안에 body의 일부분만 반환하는 summary 메소드 
    def summary(self):
        return self.body[:50]       #body 데이터를 50글자까지만 반환해라잉
    
class Comment(models.Model):
    post=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_At=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text