# Generated by Django 4.1.7 on 2023-04-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='suff_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
