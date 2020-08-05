from django.urls import path
from . import views

urlpatterns = [
	path('', views.news_list, name='news_list'),
	path('new/<int:pk>/', views.new_detail, name='new_detail'),
	path('news/add/', views.new_add, name='new_add'),
	path('news/<int:pk>/edit/', views.new_edit, name='new_edit'),
]