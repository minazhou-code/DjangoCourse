# Generated by Django 4.0.5 on 2022-06-30 19:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_alter_course_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('my_courses', django.db.models.manager.Manager()),
            ],
        ),
    ]