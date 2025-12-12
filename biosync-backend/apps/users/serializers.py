from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model, used for retrieving user profile data.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined')


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user, requires and writes the password field.
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        """Checks if passwords match."""
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        """Creates and returns a new user instance, given the validated data."""
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user
