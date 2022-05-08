from rest_framework import serializers
from testApp.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        # /--- fields : 選取要處理區欄位 exclude 選擇要排除欄位可擇一
        # fields = ['id','owner','city','activity_name','is_public','content','post_time','invitation_code']
        # excluede = []
        fields = "__all__"
    

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
        
class ColabShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColabShop
        fields = "__all__"
        
class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        
class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetail
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class ServeCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServeCity
        fields = "__all__"
        
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
        
class ShopGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopGenre
        fields = "__all__"
