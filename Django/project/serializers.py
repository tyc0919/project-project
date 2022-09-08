from rest_framework import serializers
from .models import Job, User, Activity, Collaborator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['user_email', 'password', 'avatar']
        exclude = ['password', 'enable', 'enable_time']

class UserProfileSerializer(serializers.ModelSerializer):
    # Override the model.py field, which sets null=True, so as to make the field required
    user_name = serializers.CharField(max_length=15)
    telephone = serializers.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['user_name', 'telephone']

class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'telephone']


# class UserPasswordSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = User
        # fields = ['password']


class ActivityCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ['city', 'is_public', 'is_finished', 'content', 'post_time', 'invitation_code', 'activity_description']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ['city']

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = '__all__'