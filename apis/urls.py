
from django.urls import path
from .views import DashboardStatsAPIView

urlpatterns = [
    path('', DashboardStatsAPIView.as_view(), name='dashboard-stats'),
]
