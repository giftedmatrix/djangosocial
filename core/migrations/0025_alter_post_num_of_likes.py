# Generated by Django 4.1.1 on 2023-03-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_post_num_of_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='num_of_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]