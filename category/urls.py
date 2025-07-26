from rest_framework.routers import DefaultRouter
from .views import CategoryView
from django.urls import path,include

router = DefaultRouter()
router.register(r'',CategoryView)

urlpatterns = [
    path('', include(router.urls)), 
]