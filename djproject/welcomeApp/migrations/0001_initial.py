# Generated by Django 2.2 on 2021-08-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HydJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=30)),
            ],
        ),
    ]