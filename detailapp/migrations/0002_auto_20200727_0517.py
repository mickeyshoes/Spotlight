# Generated by Django 3.0.8 on 2020-07-27 05:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detailapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like_count',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='like_dislikde',
        ),
    ]
