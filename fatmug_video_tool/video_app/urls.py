from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:video_id>/search/', views.search_video, name='search_video'),
    path('video/<int:video_id>/play/<str:timestamp>/', views.play_from_timestamp, name='play_from_timestamp'),
]