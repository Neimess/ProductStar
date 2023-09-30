from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, RepositoryModelViewSet, ItemModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('items', ItemModelViewSet)
router.register('repositories', RepositoryModelViewSet)
router.register('orders', OrderModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)
