from rest_framework.routers import DefaultRouter

from lms.views import CuratorViewSet, DirectionViewSet

lms_router = DefaultRouter()
lms_router.register(r'curator',
                        CuratorViewSet,
                        basename = 'curator')

lms_router.register(r'direction',
                    DirectionViewSet,
                    basename = 'direction')