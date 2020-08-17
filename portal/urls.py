from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url, include
from mysite import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
