from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, RegistrationSerializer

User = get_user_model()

class RegistrationView(APIView):
    """
    API view for user registration.
    POST: Creates a new User instance.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        # Validate data against RegistrationSerializer
        serializer.is_valid(raise_exception=True)
        
        # Save the new user (handling password hashing inside the serializer's create method)
        user = serializer.save()

        # You might choose to return the created user data, 
        # but often for security, a success message is sufficient, 
        # and the user must then call the /auth/token endpoint to log in.
        return Response(
            {"detail": "User registered successfully. You can now log in.", "email": user.email},
            status=status.HTTP_201_CREATED
        )


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating the authenticated user's profile.
    GET /api/v1/users/me/ : Retrieve current user profile
    PUT/PATCH /api/v1/users/me/ : Update current user profile
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Overridden to return the currently authenticated user instance.
        """
        return self.request.user

    def update(self, request, *args, **kwargs):
        # We use the get_object logic to ensure we only update the current user
        instance = self.get_object()
        
        # Use partial=True for PATCH requests
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
