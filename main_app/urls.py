from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('apps/', views.apps_index, name='index'),
    path('apps/<int:app_id>/', views.apps_detail, name='detail'),
    path('apps/create/', views.AppCreate.as_view(), name='apps_create'),
]