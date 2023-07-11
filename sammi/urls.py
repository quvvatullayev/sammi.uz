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