from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('apps/', views.apps_index, name='index'),
    path('apps/<int:app_id>/', views.apps_detail, name='detail'),
    path('apps/create/', views.AppCreate.as_view(), name='apps_create'),
    path('apps/<int:pk>/update', views.AppUpdate.as_view(), name='apps_update'),
    path('apps/<int:pk>/delete', views.AppDelete.as_view(), name='apps_delete'),
    path('apps/<int:app_id>/add_technologie/', views.add_technologie, name='add_technologie' )
]