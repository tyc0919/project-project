# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Activity(models.Model):
    owner = models.ForeignKey('User', models.DO_NOTHING, db_column='owner')
    activity_name = models.CharField(max_length=30)
    is_public = models.IntegerField(blank=True, null=True, default=0)
    is_finished = models.IntegerField(blank=True, null=True, default=0)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    invitation_code = models.CharField(max_length=20, blank=True, null=True)
    activity_picture = models.CharField(max_length=50, blank=True, null=True)
    activity_budget = models.IntegerField(blank=True, null=True)
    activity_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class Collaborator(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email')

    class Meta:
        managed = False
        db_table = 'collaborator'
        unique_together = (('activity', 'user_email'),)


class Expenditure(models.Model):
    job = models.ForeignKey('Job', models.DO_NOTHING, blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    expenditure_receipt_path = models.CharField(max_length=50, blank=True, null=True)
    expenditure_uploaded_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenditure'


class File(models.Model):
    job = models.ForeignKey('Job', models.DO_NOTHING, blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    uploader = models.ForeignKey('User', models.DO_NOTHING, db_column='uploader', blank=True, null=True)
    file_path = models.CharField(max_length=50, blank=True, null=True)
    file_uploaded_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'


class Job(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    person_in_charge_email = models.ForeignKey('User', models.DO_NOTHING, db_column='person_in_charge_email', blank=True, null=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=0)
    create_time = models.DateTimeField(blank=True, null=True)
    dead_line = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    job_budget = models.IntegerField(blank=True, null=True, default=0)
    job_expenditure = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        db_table = 'job'


class JobDetail(models.Model):
    job_detail_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    job = models.ForeignKey(Job, models.DO_NOTHING, blank=True, null=True)
    activity = models.ForeignKey(Activity, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        db_table = 'job_detail'


class Log(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email')
    action = models.CharField(max_length=50)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log'


class Review(models.Model):
    activity = models.ForeignKey(Activity, models.DO_NOTHING)
    reviewer = models.ForeignKey('User', models.DO_NOTHING, db_column='reviewer')
    content = models.CharField(max_length=500)
    review_time = models.DateTimeField(blank=True, null=True)
    review_star = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        managed = False
        db_table = 'review'


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
