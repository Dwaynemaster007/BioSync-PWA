from django.contrib import admin
from django.urls import path, include

# Import JWT views for authentication endpoints
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    # TokenVerifyView, # Optional: uncomment if you need a token verification endpoint
)

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),

    # --- API Version 1 (v1) Endpoints ---
    path('api/v1/', include([
        
        # 1. JWT Authentication Endpoints
        # POST to get access and refresh tokens (Login)
        path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        # POST to get a new access token using a refresh token
        path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        # path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Optional
        
        # 2. User & Profile Management
        # Includes /users/register/, /users/me/, etc.
        path('users/', include('apps.users.urls')),

        # 3. Activity Logging
        # Includes /activities/workouts/, /activities/biometrics/, etc.
        path('activities/', include('apps.activities.urls')),

        # Future apps like goals/workout_plans would be added here:
        # path('goals/', include('apps.goals.urls')),
    ])),
]
