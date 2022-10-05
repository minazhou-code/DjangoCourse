# Generated by Django 4.0.5 on 2022-06-10 04:06

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_desc', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=150)),
                ('duration', models.IntegerField()),
                ('delivery_mode', models.CharField(choices=[('ON', 'Online'), ('OFF', 'Offline'), ('REC', 'Recorded Session')], default='ON', max_length=3)),
                ('keywords', models.CharField(max_length=1024)),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateField(auto_now=True)),
            ],
            managers=[
                ('my_courses', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='course_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(5, 'Excellent'), (4, 'Good'), (3, 'Not bad'), (2, 'Not well'), (1, 'Poor')], default=1)),
            ],
        ),
    ]
