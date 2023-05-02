from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title
    
    #Blog 클래스 안에 body의 일부분만 반환하는 summary 메소드 
    def summary(self):
        return self.body[:50]       #body 데이터를 50글자까지만 반환해라잉