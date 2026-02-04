from django.urls import path
from .views import *
from django.views.generic.detail import DetailView
from .models import Photo
from . import views
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('upload/', Photouploadview.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', photodeleteview.as_view(), name='photo_delete'),
    path('update/<int:pk>/', photoupdateview.as_view(), name='photo_update'),
    path('detail/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('comment/like/<int:comment_id>/', views.comment_like, name='comment_like'),
    path('comment/dislike/<int:comment_id>/', views.comment_dislike, name='comment_dislike'),
]