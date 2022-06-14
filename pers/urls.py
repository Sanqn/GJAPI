from django.urls import path, include
from .views import NewPersonViewsets
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('person', NewPersonViewsets, basename='person')

urlpatterns = [
    path('', views.main, name='main'),
    path("", include(router.urls))
]