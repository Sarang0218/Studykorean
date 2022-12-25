# Generated by Django 4.1.4 on 2022-12-19 23:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_alter_question_solvedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='solvedby',
            field=models.ManyToManyField(blank=True, related_name='solvedby', to=settings.AUTH_USER_MODEL),
        ),
    ]
