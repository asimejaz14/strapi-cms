# Generated by Django 3.2.12 on 2022-03-13 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('user_apps', '0007_userapp_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='status',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='common.status'),
        ),
    ]
