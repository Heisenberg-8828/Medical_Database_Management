# Generated by Django 4.1.1 on 2022-11-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_doctorprofile_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='otp',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
