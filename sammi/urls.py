from django.urls import path
from .view.aboutimg import (
    AboutImgCreateView,
    AboutImgListView,
    AboutImgDetailView,
    AboutImgUpdateView,
    AboutImgDeleteView,
)

urlpatterns = [
    path('aboutimg/create/', AboutImgCreateView.as_view()),
    path('aboutimg/list/', AboutImgListView.as_view()),
    path('aboutimg/detail/<int:pk>/', AboutImgDetailView.as_view()),
    path('aboutimg/update/<int:pk>/', AboutImgUpdateView.as_view()),
    path('aboutimg/delete/<int:pk>/', AboutImgDeleteView.as_view()),
]

from .view.news import (
    NewsCreateView,
    NewsListView,
    NewsDetailView,
    NewsUpdateView,
    NewsDeleteView,
)

urlpatterns += [
    path('news/create/', NewsCreateView.as_view()),
    path('news/list/', NewsListView.as_view()),
    path('news/detail/<int:pk>/', NewsDetailView.as_view()),
    path('news/update/<int:pk>/', NewsUpdateView.as_view()),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view()),
]

from .view.newsimg import (
    NewsImgCreateView,
    NewsImgListView,
    NewsImgDetailView,
    NewsImgUpdateView,
    NewsImgDeleteView,
)

urlpatterns += [
    path('newsimg/create/', NewsImgCreateView.as_view()),
    path('newsimg/list/', NewsImgListView.as_view()),
    path('newsimg/detail/<int:pk>/', NewsImgDetailView.as_view()),
    path('newsimg/update/<int:pk>/', NewsImgUpdateView.as_view()),
    path('newsimg/delete/<int:pk>/', NewsImgDeleteView.as_view()),
]

from .view.video import (
    VideoCreateView,
    VideoListView,
    VideoDetailView,
    VideoUpdateView,
    VideoDeleteView,
)

urlpatterns += [
    path('video/create/', VideoCreateView.as_view()),
    path('video/list/', VideoListView.as_view()),
    path('video/detail/<int:pk>/', VideoDetailView.as_view()),
    path('video/update/<int:pk>/', VideoUpdateView.as_view()),
    path('video/delete/<int:pk>/', VideoDeleteView.as_view()),
]

