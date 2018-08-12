# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Status(models.Model):
    field_status = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'Status'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class ObsField(models.Model):
    field_no = models.IntegerField(primary_key=True)
    field_name = models.CharField(unique=True, max_length=90)
    ra = models.DecimalField(max_digits=8, decimal_places=5)
    dec = models.DecimalField(max_digits=8, decimal_places=5)
    field_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='field_status')

    class Meta:
        managed = False
        db_table = 'obs_field'
#        database = 'brite_obs'
    # necessary for converting model into something readable

    def __str__(self):
        return self.field_name

class Satellite(models.Model):
    sat_id = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'satellite'


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
    setup = models.IntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'obs_records'

    @classmethod
    def create_obsrecord(cls, record, field_no):
        db = 'brite_obs'
        obsrecord = cls()
        # change values to fit database structure
        setup = record[7][5:]
        obsrecord.star_id = record[1]
        obsrecord.star_name = record[4]
        obsrecord.sp_type = record[3]
        obsrecord.obs_start = record[8]
        obsrecord.obs_end = record[9]
        obsrecord.sat = Satellite.objects.using(db).get(sat_id=record[6])
        obsrecord.no_obs = record[11]
        obsrecord.obs_mode = record[20]
        obsrecord.setup = setup
        obsrecord.field_no = ObsField.objects.using(db).get(field_no=field_no)
#        obsrecord.sat = record[6]
        return obsrecord
