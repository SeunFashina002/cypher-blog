# Generated by Django 4.0.5 on 2022-07-01 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]