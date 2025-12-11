from django.urls import path

from .views import RegistrationView, ProfileView

# The URL patterns here are included under the 'api/v1/' prefix
urlpatterns = [
    # User Registration Endpoint: POST to create a new user
    path('users/register/', RegistrationView.as_view(), name='user_register'),
    
    # User Profile Endpoint: GET/PUT/PATCH for authenticated user's own profile
    # Uses 'me/' convention, which is common for user-specific resources
    path('users/me/', ProfileView.as_view(), name='user_profile'),
]
