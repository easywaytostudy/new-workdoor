# Generated by Django 2.2 on 2019-05-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0002_auto_20190507_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregister',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
