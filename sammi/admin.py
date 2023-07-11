from django.contrib import admin
from .models import (
    AboutImg,
    News,
    NewsImg,
    Video,
    Gallery,
    GalleryImg,
    VideoGallery,
    Ad,
    Quiz,
    UsefulSites,
    Contact,
)

# Register your models here.
admin.site.register(AboutImg)
admin.site.register(News)
admin.site.register(NewsImg)
admin.site.register(Video)
admin.site.register(Gallery)
admin.site.register(GalleryImg)
admin.site.register(VideoGallery)
admin.site.register(Ad)
admin.site.register(Quiz)
admin.site.register(UsefulSites)
admin.site.register(Contact)

