from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from shop.models import Shop
from shop.permissions import IsOwnerOrReadOnly
from shop.serializer import ShopSerializer


# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    """ view to create update and return a shop. """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
