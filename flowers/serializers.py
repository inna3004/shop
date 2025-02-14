from rest_framework import routers, serializers, viewsets
from flowers.models import Flower


# для api
class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'discount']
