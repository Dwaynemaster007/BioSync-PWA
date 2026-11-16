from rest_framework.routers import DefaultRouter

from .views import GoalViewSet

# /api/v1/goals/ (list, create) and /api/v1/goals/{pk}/ (retrieve, update, delete)
router = DefaultRouter()
router.register(r'', GoalViewSet, basename='goal')

urlpatterns = router.urls
