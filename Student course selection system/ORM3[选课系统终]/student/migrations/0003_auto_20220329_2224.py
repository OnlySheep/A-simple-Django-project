# Generated by Django 3.2.1 on 2022-03-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220329_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='classAddr',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='classTime',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=3, verbose_name='学分'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
