from django.urls import path, include
from rest_framework import routers

from shop.views import ShopDetailView

router = routers.DefaultRouter()
router.register('shops', ShopDetailView, basename='shop')
app_name = 'shop'
urlpatterns = [
    path('', include(router.urls))
]
