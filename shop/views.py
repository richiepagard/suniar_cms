from rest_framework import permissions, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from shop.permissions import IsOwnerOrReadOnly
from shop.serializer import ShopSerializer, ShopListSerializer


# Create your views here.
class ShopListView(generics.ListAPIView):
    """ view to return list of shops for authenticated users. """
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = []


class ShopDetailView(RetrieveUpdateDestroyAPIView):
    """ Retrieve ,Update ,Destroy a shop just for its owner. """
    serializer_class = ShopListSerializer
    permission_classes = [IsOwnerOrReadOnly]
