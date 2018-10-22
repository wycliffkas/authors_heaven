from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.AritcleView)

urlpatterns = [
    path('', include(router.urls))
   
]  