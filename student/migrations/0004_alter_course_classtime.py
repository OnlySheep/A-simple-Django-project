# Generated by Django 3.2.1 on 2022-03-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20220329_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='classTime',
            field=models.DateField(null=True),
        ),
    ]
