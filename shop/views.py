from rest_framework import viewsets

from shop.models import Shop
from shop.permissions import IsOwnerOrReadOnly
from shop.serializer import ShopSerializer


# Create your views here.
# class ShopListView(generics.ListAPIView):
#     """ view to return list of shops for authenticated users. """
#     serializer_class = ShopSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [IsOwnerOrReadOnly]


class ShopDetailView(viewsets.ModelViewSet):
    """ Retrieve ,Update ,Destroy a shop just for its owner. """

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsOwnerOrReadOnly]
