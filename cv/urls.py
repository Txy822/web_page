
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('cv/new/', views.cv_new, name='cv_new'),
    path('cv/<int:pk>/edit/', views.cv_edit, name='cv_edit'),
    path('cvt/<pk>/remove/', views.cv_remove, name='cv_remove'),
]
