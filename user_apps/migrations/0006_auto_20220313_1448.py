# Generated by Django 3.2.12 on 2022-03-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_apps', '0005_subscription_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapp',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userapp',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
