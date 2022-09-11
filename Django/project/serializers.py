from rest_framework import serializers
from .models import Job, User, Activity, Collaborator
from .modules import db_password_generator, salt_generator


# -----UserProfile START-----
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
    password = serializers.CharField(min_length=1)
    
    def update(self, instance, validated_data):
        new_password = validated_data["password"]
        hashed_password = db_password_generator(password=new_password,salt=salt_generator())
        instance.password = hashed_password
        instance.save()
        return instance

        
    class Meta:
        model = User
        fields = ['password']

# -----UserProfile END-----
# -----Activity START-----

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

class ActivityBudgetSerializer(serializers.ModelSerializer):  #WIP
    activity_budget = serializers.IntegerField(min_value=0)
    class Meta:
        model = Activity
        fields = ['activity_budget']

class ActivityUpdateSerializer(serializers.ModelSerializer):  #WIP

    activity_budget = serializers.IntegerField(min_value=0, default=0)
    activity_name = serializers.CharField(min_length=3, max_length=30)

    class Meta:
        model = Activity
        fields = ['owner','activity_name', 'activity_budget', 'activity_description']

    def create(self, validated_data):   #Need to add the owner into collaborators as well, so I override the create() method
        activity = Activity.objects.create(**validated_data)
        Collaborator(activity=activity, user_email=validated_data["owner"]).save()
        return activity
    
    def update(self, instance, validated_data): # Some parameters are needed, and must be ignored so that I don't have to code another serializer
        instance.activity_name = validated_data["activity_name"]
        instance.activity_description = validated_data["activity_description"]
        instance.save()
        return instance

class ActivityPublishSerializer(serializers.ModelSerializer):
    is_public = serializers.IntegerField(min_value=0, max_value=1)
    class Meta:
        model = Activity
        fields = ['is_public']

class ActivityFinishSerializer(serializers.ModelSerializer):
    is_finished = serializers.IntegerField(min_value=0, max_value=1)
    class Meta:
        model = Activity
        fields = ['is_finished']

# -----Activity END-----