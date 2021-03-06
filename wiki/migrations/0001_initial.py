# Generated by Django 2.0.7 on 2018-07-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        # migrations.CreateModel(
        #     name='ObsField',
        #     fields=[
        #         ('field_no', models.IntegerField(primary_key=True, serialize=False)),
        #         ('field_name', models.CharField(max_length=90, unique=True)),
        #         ('ra', models.DecimalField(decimal_places=5, max_digits=8)),
        #         ('dec', models.DecimalField(decimal_places=5, max_digits=8)),
        #     ],
        #     options={
        #         'db_table': 'obs_field',
        #         'managed': False,
        #     },
        # ),
        # migrations.CreateModel(
        #     name='ObsRecords',
        #     fields=[
        #         ('idobs_records', models.AutoField(primary_key=True, serialize=False)),
        #         ('star_id', models.CharField(max_length=45)),
        #         ('star_name', models.CharField(blank=True, max_length=45, null=True)),
        #         ('sp_type', models.CharField(blank=True, max_length=45, null=True)),
        #         ('obs_start', models.CharField(max_length=45)),
        #         ('obs_end', models.CharField(max_length=45)),
        #         ('no_obs', models.IntegerField()),
        #         ('obs_mode', models.CharField(max_length=10)),
        #         ('availability', models.CharField(max_length=45)),
        #     ],
        #     options={
        #         'db_table': 'obs_records',
        #         'managed': False,
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Satellite',
        #     fields=[
        #         ('sat_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
        #     ],
        #     options={
        #         'db_table': 'satellite',
        #         'managed': False,
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Status',
        #     fields=[
        #         ('field_status', models.CharField(max_length=45, primary_key=True, serialize=False)),
        #     ],
        #     options={
        #         'db_table': 'Status',
        #         'managed': False,
        #    },
        #),
    ]
