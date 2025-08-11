from rest_framework import serializers

from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """
    Serializer for Shop.
    """
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Shop
        exclude = ['created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
