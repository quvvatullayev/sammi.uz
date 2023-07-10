from django.db import models

class AboutImg(models.Model):
    img = models.ImageField(upload_to='about_img')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class News(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sees = models.IntegerField(default=0)
    img = models.ImageField(upload_to='news_img')

    def __str__(self):
        return self.name
