
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    owner = models.ForeignKey('User', models.DO_NOTHING, db_column='owner')
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city', blank=True, null=True)
    activity_name = models.CharField(max_length=30)
    is_public = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    invitation_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_name = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class ColabShop(models.Model):
    id = models.IntegerField(primary_key=True)
    shop_account = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_account', blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colab_shop'


class Collaborator(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    user_account = models.ForeignKey('User', models.DO_NOTHING, db_column='user_account')

    class Meta:
        managed = False
        db_table = 'collaborator'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Job(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    person_in_charge_account = models.ForeignKey('User', models.DO_NOTHING, db_column='person_in_charge_account', blank=True, null=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    order = models.IntegerField(unique=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    dead_line = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class JobDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.ForeignKey(Job, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    order = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'job_detail'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    reviewer = models.ForeignKey('User', models.DO_NOTHING, db_column='reviewer', blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    review_time = models.DateTimeField(blank=True, null=True)
    review_star = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class ServeCity(models.Model):
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)
    shop_account = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_account', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serve_city'


class Shop(models.Model):
    account = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=70, blank=True, null=True)
    contact_person = models.CharField(max_length=15, blank=True, null=True)
    shop_name = models.CharField(max_length=30, blank=True, null=True)
    genre = models.ForeignKey('ShopGenre', models.DO_NOTHING, db_column='genre', blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    picture_path = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class ShopGenre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_genre'


class User(models.Model):
    account = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=70, blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    picture_path = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
