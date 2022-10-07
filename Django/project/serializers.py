import datetime
from rest_framework import serializers
from django.utils import timezone
from .models import Expenditure, Job, Review, User, Activity, Collaborator, JobDetail, File
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

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_email', 'user_name', 'picture_path', 'telephone']

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

# Job validator
def activity_exsists(value):
    try:
        Activity.objects.get(pk=value)
    except:
        raise serializers.ValidationError('無此活動')

def valid_datetime(value):
    if value < timezone.now(): raise serializers.ValidationError('截止日期必須大於今天')

def valid_user(value):
    try:
        User.objects.get(pk=value)
    except:
        raise serializers.ValidationError('使用者不存在')
# Job validator end

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobCreateSerializer(serializers.ModelSerializer):
    activity_id = serializers.IntegerField(validators=[activity_exsists])
    person_in_charge_email = serializers.EmailField(validators=[valid_user])
    dead_line = serializers.DateTimeField(validators=[valid_datetime])
    content = serializers.CharField(max_length=500, default="")
    job_budget = serializers.IntegerField(min_value=0, default=0)

    class Meta:
        model = Job
        exclude = ['activity', 'status', 'create_time', 'job_expenditure']
    
    def create(self, validated_data): 
        data = {
            "activity": Activity.objects.get(pk=validated_data.get("activity_id")),
            "person_in_charge_email": User.objects.get(pk=validated_data.get("person_in_charge_email")),
            "title": validated_data.get("title"),
            "create_time": timezone.now(),
            "dead_line": validated_data.get("dead_line"),
            "content": validated_data.get("content"),
            "job_budget": validated_data.get("job_budget"),
            "job_expenditure": 0
        }

        print(data.get("create_time"))
        print(data.get("dead_line"))
        return Job.objects.create(**data)
        
class JobUpdateSerializer(serializers.ModelSerializer):
    person_in_charge_email = serializers.EmailField(validators=[valid_user])
    dead_line = serializers.DateTimeField(validators=[valid_datetime])
    title = serializers.CharField(max_length=15)
    content = serializers.CharField(max_length=15)
    job_budget = serializers.IntegerField(min_value=0)
    job_expenditure = serializers.IntegerField(min_value=0)

    class Meta:
        model = Job
        fields = ['person_in_charge_email', 'title', 'dead_line', 'content', 'job_budget', 'job_expenditure']

    def update(self, instance, validated_data):
        instance.person_in_charge_email = User.objects.get(user_email=validated_data.get("person_in_charge_email"))
        instance.dead_line = validated_data.get("dead_line")
        instance.title = validated_data.get("title")
        instance.content = validated_data.get("content")
        instance.job_budget = validated_data.get("job_budget")
        instance.job_expenditure = validated_data.get("job_expenditure")
        instance.save(update_fields=[
            'person_in_charge_email',
            'dead_line',
            'title',
            'content',
            'job_budget',
            'job_expenditure'
            ])
        # data = {
            # "person_in_charge_email": User.objects.get(pk=validated_data.get("person_in_charge_email")),
            # "title": validated_data.get("title"),
            # "dead_line": validated_data.get("dead_line"),
            # "content": validated_data.get("content"),
            # "job_budget": validated_data.get("job_budget"),
            # "job_expenditure": 0
        # }

        return instance

class JobStatusSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(min_value=0, max_value=1)
    class Meta:
        model = Job
        fields = ['status']
    def update(self, instance, validated_data):
        instance.status = validated_data.get("status")
        instance.save(update_fields=['status'])
        return instance


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = '__all__'


class JobDetailCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=15)
    content = serializers.CharField(default="")
    job_id = serializers.IntegerField()
    class Meta:
        model = JobDetail
        fields = ['content', 'job_id', 'title']

    def create(self, validated_data):   #Need to add the owner into collaborators as well, so I override the create() method
        job = Job.objects.get(pk=validated_data.get("job_id"))
        jd = JobDetail.objects.create(
            job=job,
            activity=job.activity,
            content=validated_data.get("content"),
            title=validated_data.get("title"))
        return jd

class JobDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = ['content', 'title']

class JobDetailStatusSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(min_value=0, max_value=1)
    class Meta:
        model = JobDetail
        fields = ['status']

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

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


# -----Activity END-----
# -----Social START-----
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ['city', 'invitation_code', 'is_public']

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Review
        fields = '__all__'


# -----Social END-----