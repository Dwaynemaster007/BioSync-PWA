"""
URL configuration for biosync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Import JWT views for token management
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Configuration for static and media files (only needed for local development)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),

    # Core Authentication Routes (JWT)
    # Allows users to exchange credentials for access and refresh tokens
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Allows users to refresh their access token using their refresh token
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Allows verification of the token validity
    path('api/v1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Application-Specific API Routes (API Version 1)
    # All custom app URLs will be nested under this path
    path('api/v1/', include('apps.users.urls')),          # User registration and profile
    # path('api/v1/', include('apps.activities.urls')),   # Workouts, Exercises, Biometrics (to be added)
    # path('api/v1/', include('apps.goals.urls')),        # Goals (to be added)
    # path('api/v1/', include('apps.workout_plans.urls')),# Workout Plans (to be added)
]

# Serve media files (like profile pictures) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
