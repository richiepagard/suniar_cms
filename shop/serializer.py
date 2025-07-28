from rest_framework import serializers

from models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """ Serializer for Shop. """

    class Meta:
        model = Shop
        fields = ['name', 'owner', 'work_field', 'date_created']
        read_only_fields = ['id', 'owner', 'date_created']
