from rest_framework import viewsets

# Create your views here.
from lms.models import Curator, Direction, Student, Disciplina, Group
from lms.serializer import CuratorSerializer, DirectionSerializer, StudentSerializer, DisciplinaSerializer, GroupSerializer
from lms.permissions import IsAdminOrReadOnly, IsCuratorOrReadOnly

class CuratorViewSet(viewsets.ModelViewSet):

    queryset = Curator.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminOrReadOnly]

class DirectionViewSet(viewsets.ModelViewSet):

    queryset = Direction.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorOrReadOnly]


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = DisciplinaSerializer
    permission_classes = [IsCuratorOrReadOnly]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [IsCuratorOrReadOnly]
