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
    is_finished = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    invitation_code = models.CharField(max_length=20, blank=True, null=True)
    activity_picture = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class City(models.Model):
    city_name = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class CollabShop(models.Model):
    id = models.IntegerField(primary_key=True)
    shop_email = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_email', blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    shop_permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collab_shop'


class Collaborator(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'collaborator'


class Job(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    person_in_charge_email = models.ForeignKey('User', models.DO_NOTHING, db_column='person_in_charge_email', blank=True, null=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    order = models.IntegerField(unique=True)
    status = models.ForeignKey('JobStatus', models.DO_NOTHING, db_column='status', blank=True, null=True)
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


class JobStatus(models.Model):
    status_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_status'


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
    shop_email = models.ForeignKey('Shop', models.DO_NOTHING, db_column='shop_email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serve_city'


class Shop(models.Model):
    shop_email = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=130, blank=True, null=True)
    contact_person = models.CharField(max_length=15, blank=True, null=True)
    shop_name = models.CharField(max_length=30, blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    picture_path = models.CharField(max_length=50, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    enable_time = models.DateTimeField(blank=True, null=True)
    genre = models.ForeignKey('ShopGenre', models.DO_NOTHING, db_column='genre', blank=True, null=True)

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
    user_email = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=130, blank=True, null=True)
    user_name = models.CharField(max_length=15, blank=True, null=True)
    picture_path = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    enable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
