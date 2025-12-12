from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, ProgressRecordViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'progress', ProgressRecordViewSet, basename='progress')

# The API URLs are now determined automatically by the router.
# We include the root level routes here.
urlpatterns = [
    path('', include(router.urls)),
]
