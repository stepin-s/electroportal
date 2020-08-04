from django.urls import path
from . import views

urlpatterns = [
	path('', views.news_list, name='news_list'),
	path('new/<int:pk>/', views.new_detail, name='new_detail'),
]