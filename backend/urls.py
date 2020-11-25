"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .api.views import index_view
from .api import views

router = routers.DefaultRouter()
router.register('personal_information', views.PIViewSet)
router.register('department_information', views.DIViewSet)
router.register('medical_information', views.MIViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    path('api/login/', views.login),

    path('api/register/', views.register),

]
