from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['user_email', 'password', 'avatar']
        exclude = ['password', 'enable', 'enable_time']