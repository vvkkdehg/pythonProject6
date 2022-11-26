from rest_framework import serializers

from lms.models import Curator, Direction

class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = '__all__'

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'
