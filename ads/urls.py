from django.urls import path
from .views import AdDetailView, AdListView

urlpatterns = [
    path('', AdListView.as_view(), name='ad-list'),
    path('<int:ad_id>/', AdDetailView.as_view(), name='ad-detail'),
]
