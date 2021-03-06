# Generated by Django 2.2 on 2019-05-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0003_auto_20190509_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='registered',
            field=models.CharField(default='False', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidatenotifications',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companyregister',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobnotifications',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
