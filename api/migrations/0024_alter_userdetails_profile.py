# Generated by Django 4.1.7 on 2023-04-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_userdetails_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
