from django.db import models

class AboutImg(models.Model):
    img = models.ImageField(upload_to='about_img')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name