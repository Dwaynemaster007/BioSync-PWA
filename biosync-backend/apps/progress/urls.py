from rest_framework.routers import DefaultRouter
from .views import ProgressEntryViewSet

router = DefaultRouter()
router.register(r'', ProgressEntryViewSet, basename='progressentry')

urlpatterns = router.urls
