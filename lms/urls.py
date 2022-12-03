from rest_framework.routers import DefaultRouter

from lms.views import CuratorViewSet, DirectionViewSet, StudentViewSet, DisciplinaViewSet, GroupViewSet

lms_router = DefaultRouter()
lms_router.register(r'curator',
                        CuratorViewSet,
                        basename = 'curator')

lms_router.register(r'direction',
                    DirectionViewSet,
                    basename = 'direction')

lms_router.register(r'students',
                    StudentViewSet,
                    basename = 'students')

lms_router.register(r'disciplina',
                    DisciplinaViewSet,
                    basename = 'disciplina')

lms_router.register(r'group',
                    GroupViewSet,
                    basename = 'group')