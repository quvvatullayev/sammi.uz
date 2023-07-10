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
    
class NewsImg(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='news_img')

    def __str__(self):
        return self.news.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery_img')
    created_at = models.DateTimeField(auto_now_add=True)
    sees = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class GalleryImg(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery_img')

    def __str__(self):
        return self.gallery.name

class VideoGallery(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    sees = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    sees = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

