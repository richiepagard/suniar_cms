from rest_framework import serializers

from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """ Serializer for Shop. """
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'work_field', 'date_created', 'category']
        read_only_fields = ['id', 'owner', 'date_created']
