from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkoutViewSet, BiometricDataViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
# This creates endpoints like /api/v1/activities/workouts/ and /api/v1/activities/workouts/{pk}/
router.register(r'workouts', WorkoutViewSet, basename='workout')

# This creates endpoints like /api/v1/activities/biometrics/ and /api/v1/activities/biometrics/{pk}/
router.register(r'biometrics', BiometricDataViewSet, basename='biometricdata')

# The API URLs are now determined automatically by the router.
# The `activities/` prefix will be added in the main project urls.py
urlpatterns = [
    path('', include(router.urls)),
]
