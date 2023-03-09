# Generated by Django 4.1.1 on 2023-03-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_background_profile_pics_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_profile_pics',
            field=models.ImageField(default='s3://djangosocial/bg_profile_pics/defaultimage.jpg', upload_to='bg_profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(default='s3://djangosocial/profile_pics/defaultimage2.jpg', upload_to='profile_pics'),
        ),
    ]
