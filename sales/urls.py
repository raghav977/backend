from django.urls import path,include

from rest_framework import routers
from sales.views import SaleViewSet
router = routers.DefaultRouter()

router.register(r'',SaleViewSet)
urlpatterns = [
    path('',include(router.urls))
]
