# Generated by Django 5.1.4 on 2024-12-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0002_remove_post_categories_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
