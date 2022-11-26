from rest_framework import viewsets

# Create your views here.
from lms.models import Curator, Direction
from lms.serializer import CuratorSerializer, DirectionSerializer


class CuratorViewSet(viewsets.ModelViewSet):

    queryset = Curator.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = CuratorSerializer

class DirectionViewSet(viewsets.ModelViewSet):

    queryset = Direction.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = DirectionSerializer