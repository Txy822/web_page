
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_section_list, name='cv_section_list'),
    path('cv/<int:pk>/', views.cv_section_detail, name='cv_section_detail'),
    path('cv/new/', views.cv_section_new, name='cv_section_new'),
    path('cv/<int:pk>/edit/', views.cv_section_edit, name='cv_section_edit'),
    path('cv/<pk>/remove/', views.cv_section_remove, name='cv_section_remove'),
]
