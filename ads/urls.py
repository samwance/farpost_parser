from django.urls import path
from .views import AdDetailView

urlpatterns = [
    path('ads/<int:ad_id>/', AdDetailView.as_view(), name='ad-detail'),
]
