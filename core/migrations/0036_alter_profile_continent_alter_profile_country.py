# Generated by Django 4.1.1 on 2023-03-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_profile_username_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='continent',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
