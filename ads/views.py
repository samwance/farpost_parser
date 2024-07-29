from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad
from .serializers import AdSerializer


class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'
    permission_classes = [IsAuthenticated]
