from django.urls import path
from . import views

urlpatterns = [
	path('', views.news_list, name='news_list'),
	path('new/<int:pk>/', views.new_detail, name='new_detail'),
	path('news/add/', views.new_add, name='new_add'),
	path('news/<int:pk>/edit/', views.new_edit, name='new_edit'),
	path('video/<int:pk>/', views.video_detail, name='video_detail'),
	path('videos/add/', views.video_add, name='video_add'),
	path('videos/<int:pk>/edit/', views.video_edit, name='video_edit'),
	path('videos/', views.videos_list, name='videos_list'),
]