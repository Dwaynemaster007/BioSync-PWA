from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),

    # Django REST Framework Authentication routes (for login/logout)
    path('auth/', include('rest_framework.urls')),

    # API Endpoints for the 'progress' application
    path('api/v1/', include('apps.progress.urls')),
]
