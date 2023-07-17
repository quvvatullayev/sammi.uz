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

from .view.gallery import (
    GalleryCreateView,
    GalleryListView,
    GalleryDetailView,
    GalleryUpdateView,
    GalleryDeleteView,
)

urlpatterns += [
    path('gallery/create/', GalleryCreateView.as_view()),
    path('gallery/list/', GalleryListView.as_view()),
    path('gallery/detail/<int:pk>/', GalleryDetailView.as_view()),
    path('gallery/update/<int:pk>/', GalleryUpdateView.as_view()),
    path('gallery/delete/<int:pk>/', GalleryDeleteView.as_view()),
]

from .view.galleryimg import (
    GalleryImgCreateView,
    GalleryImgListView,
    GalleryImgDetailView,
    GalleryImgUpdateView,
    GalleryImgDeleteView,
)

urlpatterns += [
    path('galleryimg/create/', GalleryImgCreateView.as_view()),
    path('galleryimg/list/', GalleryImgListView.as_view()),
    path('galleryimg/detail/<int:pk>/', GalleryImgDetailView.as_view()),
    path('galleryimg/update/<int:pk>/', GalleryImgUpdateView.as_view()),
    path('galleryimg/delete/<int:pk>/', GalleryImgDeleteView.as_view()),
]

from .view.videogallery import (
    VideoGalleryCreateView,
    VideoGalleryListView,
    VideoGalleryDetailView,
    VideoGalleryUpdateView,
    VideoGalleryDeleteView,
)

urlpatterns += [
    path('videogallery/create/', VideoGalleryCreateView.as_view()),
    path('videogallery/list/', VideoGalleryListView.as_view()),
    path('videogallery/detail/<int:pk>/', VideoGalleryDetailView.as_view()),
    path('videogallery/update/<int:pk>/', VideoGalleryUpdateView.as_view()),
    path('videogallery/delete/<int:pk>/', VideoGalleryDeleteView.as_view()),
]

from .view.ad import (
    AdCreateView,
    AdListView,
    AdDetailView,
    AdUpdateView,
    AdDeleteView,
)

urlpatterns += [
    path('ad/create/', AdCreateView.as_view()),
    path('ad/list/', AdListView.as_view()),
    path('ad/detail/<int:pk>/', AdDetailView.as_view()),
    path('ad/update/<int:pk>/', AdUpdateView.as_view()),
    path('ad/delete/<int:pk>/', AdDeleteView.as_view()),
]

from .view.mainstatistic import (
    MainStatisticCreateViews,
    MainStatisticListViews,
    MainStatisticDetailViews,
    MainStatisticUpdateViews,
    MainStatisticDeleteViews,
)

urlpatterns += [
    path('mainstatistic/create/', MainStatisticCreateViews.as_view()),
    path('mainstatistic/list/', MainStatisticListViews.as_view()),
    path('mainstatistic/detail/<int:pk>/', MainStatisticDetailViews.as_view()),
    path('mainstatistic/update/<int:pk>/', MainStatisticUpdateViews.as_view()),
    path('mainstatistic/delete/<int:pk>/', MainStatisticDeleteViews.as_view()),
]

from .view.quiz import (
    QuizCreateViews,
    QuizListViews,
    QuizDetailViews,
    QuizUpdateViews,
    QuizDeleteViews,
)

urlpatterns += [
    path('quiz/create/', QuizCreateViews.as_view()),
    path('quiz/list/', QuizListViews.as_view()),
    path('quiz/detail/<int:pk>/', QuizDetailViews.as_view()),
    path('quiz/update/<int:pk>/', QuizUpdateViews.as_view()),
    path('quiz/delete/<int:pk>/', QuizDeleteViews.as_view()),
]

from .view.usefulsites import (
    UsefulSitesCreateViews,
    UsefulSitesListViews,
    UsefulSitesDetailViews,
    UsefulSitesUpdateViews,
    UsefulSitesDeleteViews,
)

urlpatterns += [
    path('usefulsites/create/', UsefulSitesCreateViews.as_view()),
    path('usefulsites/list/', UsefulSitesListViews.as_view()),
    path('usefulsites/detail/<int:pk>/', UsefulSitesDetailViews.as_view()),
    path('usefulsites/update/<int:pk>/', UsefulSitesUpdateViews.as_view()),
    path('usefulsites/delete/<int:pk>/', UsefulSitesDeleteViews.as_view()),
]

from .view.usefulsites import (
    UsefulSitesCreateViews,
    UsefulSitesListViews,
    UsefulSitesDetailViews,
    UsefulSitesUpdateViews,
    UsefulSitesDeleteViews,
)

urlpatterns += [
    path('usefulsites/create/', UsefulSitesCreateViews.as_view()),
    path('usefulsites/list/', UsefulSitesListViews.as_view()),
    path('usefulsites/detail/<int:pk>/', UsefulSitesDetailViews.as_view()),
    path('usefulsites/update/<int:pk>/', UsefulSitesUpdateViews.as_view()),
    path('usefulsites/delete/<int:pk>/', UsefulSitesDeleteViews.as_view()),
]

from .view.contact import (
    ContactCreateView,
    ContactListView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView,
)

urlpatterns += [
    path('contact/create/', ContactCreateView.as_view()),
    path('contact/list/', ContactListView.as_view()),
    path('contact/detail/<int:pk>/', ContactDetailView.as_view()),
    path('contact/update/<int:pk>/', ContactUpdateView.as_view()),
    path('contact/delete/<int:pk>/', ContactDeleteView.as_view()),
]

from .view.home import (
    HomeViews,
)

urlpatterns += [
    path('home/', HomeViews.as_view()),
]

from .view.user import (
    UserCreateView,
    UserLoginView,
    UserLogoutView,
    UserCreateAdminView,
    UserDeleteAdminView,
    UserAdminListView,
    UserNontAdminListView,
)

urlpatterns += [
    path('user/create/', UserCreateView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', UserLogoutView.as_view()),
    path('user/createadmin/<int:pk>/', UserCreateAdminView.as_view()),
    path('user/deleteadmin/<int:pk>/', UserDeleteAdminView.as_view()),
    path('user/adminlist/', UserAdminListView.as_view()),
    path('user/nontadminlist/', UserNontAdminListView.as_view()),
]




