from rest_framework import viewsets

from shop.models import Shop
from shop.permissions import IsOwnerOrReadOnly
from shop.serializer import ShopSerializer


class ShopDetailView(viewsets.ModelViewSet):
    """ Retrieve ,Update ,Destroy a shop just for its owner. """

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsOwnerOrReadOnly]
