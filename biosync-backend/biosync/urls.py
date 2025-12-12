from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Django Admin Site
    path('admin/', admin.site.urls),

    # 2. REST Framework Authentication Routes (for basic login/logout via browser)
    path('auth/', include('rest_framework.urls')),

    # 3. API Version 1 Endpoints
    path('api/v1/', include([
        # User Authentication and Management (e.g., register, login, profile)
        path('users/', include('apps.users.urls')),

        # Goals Management (Goals API is defined using a router)
        path('', include('apps.goals.routers')),

        # Progress Tracking (Courses, Lessons, and Progress Records)
        path('', include('apps.progress.urls')),
    ])),
]
