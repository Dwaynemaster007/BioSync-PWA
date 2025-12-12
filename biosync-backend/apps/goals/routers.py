from rest_framework.routers import DefaultRouter
from apps.goals.views import GoalViewSet

# Create a router instance
router = DefaultRouter()

# Register the GoalViewSet
# This automatically generates routes like:
# /api/goals/ - List and Create
# /api/goals/{pk}/ - Retrieve, Update, and Destroy
router.register(r'goals', GoalViewSet, basename='goal')

# The urlpatterns will be included in the main project URLs.
urlpatterns = router.urls
