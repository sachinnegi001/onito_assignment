"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# /api/v1/longest-duration-movies
#  /api/v1/top-rated-movies
# /api/v1/new-movie
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('longest-duration-movies/',views.movielist.as_view()),
    path('top-rated-movies/',views.ratinglist.as_view()),
    path('new-movie/',views.Movielist.as_view()),
    path('adding_csv_fileto_movies/', views.UploadFileViewtomovies.as_view(), name='upload-file'),
    path('adding_csv_fileto_ratings/', views.UploadFileViewtoratings.as_view(), name='upload-file'),

]
