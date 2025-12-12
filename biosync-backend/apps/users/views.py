from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer, UserRegistrationSerializer
from .models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    """
    Registers a new user and automatically generates and returns an authentication token.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate token for the newly registered user
        token, created = Token.objects.get_or_create(user=user)
        
        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': CustomUserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginView(APIView):
    """
    Authenticates a user via email/username and password, and returns the authentication token.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email') # Allow login via email or username
        password = request.data.get('password')

        user = None
        if email:
            try:
                # Attempt to retrieve user by email
                user = CustomUser.objects.get(email__iexact=email)
            except CustomUser.DoesNotExist:
                pass # Continue to check by username if not found by email

        # If not found by email, or if username was provided directly
        if not user and username:
            user = CustomUser.objects.filter(username__iexact=username).first()

        if user and user.check_password(password):
            # Authentication successful
            Token.objects.filter(user=user).delete() # Invalidate old token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': CustomUserSerializer(user).data,
                'token': token.key
            })
        
        # Authentication failed
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View to retrieve and update the authenticated user's profile.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
