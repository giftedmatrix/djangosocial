# Generated by Django 4.1.1 on 2023-03-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_of_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
