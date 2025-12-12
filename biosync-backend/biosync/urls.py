from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Django Admin Site
    path('admin/', admin.site.urls),

    # 2. REST Framework Authentication Routes (for basic login/logout via browser)
    path('auth/', include('rest_framework.urls')),

    # 3. # API Version 1 Routes
    path('api/v1/', include([
        # User Authentication and Profile Management
        path('users/', include('apps.users.urls')), # <-- NEW: User auth URLs

        # Goals and Progress
        path('goals/', include('apps.goals.urls')),
        path('progress/', include('apps.progress.urls')), # Uncomment when Progress app is ready
    ])),
]
