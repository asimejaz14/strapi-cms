# Generated by Django 3.1.7 on 2022-03-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_apps', '0002_alter_subscriptionplan_plan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
