# Generated by Django 4.1.5 on 2023-01-31 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_gallery_alter_post_options_alter_post_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
