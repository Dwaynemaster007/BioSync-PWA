from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Retrieve the custom User model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, used for retrieving and updating profile data.
    Excludes sensitive fields like password.
    """
    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 
            'bio', 'profile_picture', 'fitness_level', 
            'height_cm', 'latest_weight_kg', 'date_of_birth', 
            'is_staff', 'is_active', 'date_joined', 'last_login',
        )
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined', 'last_login')


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer used for user registration (POST /api/v1/users/register).
    Handles password validation and hashing upon creation.
    """
    password2 = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True, 
        label=_('Confirm Password')
    )

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'password2', 
            'first_name', 'last_name'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        """
        Validate that the two password fields match.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "The two password fields did not match."})
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance, setting the hashed password.
        """
        # Remove confirmation password field
        validated_data.pop('password2')
        
        # Create user with set_password() to ensure hashing
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user
