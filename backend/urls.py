from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .api.views import index_view
from .api import views

router = routers.DefaultRouter()
router.register(r'personal_information', views.PIViewSet)
router.register(r'department_information', views.DIViewSet)
router.register(r'medical_information', views.MIViewSet)
router.register(r'medical_record', views.MRViewSet)

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
