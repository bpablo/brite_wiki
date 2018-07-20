# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Status(models.Model):
    field_status = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = True
        db_table = 'Status'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class ObsField(models.Model):
    field_no = models.IntegerField(primary_key=True)
    field_name = models.CharField(unique=True, max_length=90)
    ra = models.DecimalField(max_digits=8, decimal_places=5)
    dec = models.DecimalField(max_digits=8, decimal_places=5)
    field_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='field_status')

    class Meta:
        managed = True
        db_table = 'obs_field'


class ObsRecords(models.Model):
    idobs_records = models.AutoField(primary_key=True)
    star_id = models.CharField(max_length=45)
    star_name = models.CharField(max_length=45, blank=True, null=True)
    sp_type = models.CharField(max_length=45, blank=True, null=True)
    obs_start = models.CharField(max_length=45)
    obs_end = models.CharField(max_length=45)
    sat = models.ForeignKey('Satellite', models.DO_NOTHING)
    no_obs = models.IntegerField()
    obs_mode = models.CharField(max_length=10)
    availability = models.CharField(max_length=45)
    field_no = models.ForeignKey(ObsField, models.DO_NOTHING, db_column='field_no')

    class Meta:
        managed = True
        db_table = 'obs_records'


class Satellite(models.Model):
    sat_id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = True
        db_table = 'satellite'
