from django.contrib import admin

from testApp.models import * 
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['account']
    
class ShopAdmin(admin.ModelAdmin):
    list_display = ['account']

class ColabShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_account','activity']
    
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'activity','user_account']
    
class ShopGenreAdmin(admin.ModelAdmin):
    list_display = ['id','genre']
    
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_name']
    
class ServeCityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']
    
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'activity_name', 'owner', 'city']
    
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'activity',]
    
class JobDetailAdmin(admin.ModelAdmin):
    list_display = ['id','job','content']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','activity','reviewer']

list = [
    User,Shop,Collaborator,ColabShop,ShopGenre,
    City,ServeCity,
    Activity,Job,JobDetail,Review
]

adminList = [
    UserAdmin,ShopAdmin,CollaboratorAdmin,ColabShopAdmin,ShopGenreAdmin,
    CityAdmin,ServeCityAdmin,
    ActivityAdmin,JobAdmin,JobDetailAdmin,ReviewAdmin
]

for index in range(len(list)):
    modelName = list[index]
    style = adminList[index]
    admin.site.register(modelName,style)
    

