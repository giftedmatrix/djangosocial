# Generated by Django 4.1.1 on 2023-03-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_user_images_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_profile_pics',
            field=models.ImageField(default='background_profile_pics/defaultimage.jpg', upload_to='bg_profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pics',
            field=models.ImageField(default='profile_pics/defaultimage2.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='User_images',
        ),
    ]
