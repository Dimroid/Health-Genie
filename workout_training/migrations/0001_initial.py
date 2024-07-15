# Generated by Django 5.0.6 on 2024-06-05 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('symptom_checker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(help_text='Body height in meters')),
                ('age', models.IntegerField(help_text='Age in years')),
                ('mass', models.FloatField(help_text='Body mass in kilograms')),
                ('body_fat', models.FloatField(blank=True, help_text='Body fat percentage', null=True)),
                ('workout_intensity', models.CharField(choices=[('INTENSE', 'Intense'), ('NORMAL', 'Normal'), ('BODYBUILDING', 'Bodybuilding'), ('CALISTHENICS', 'Calisthenics'), ('OTHER', 'Other')], default='NORMAL', max_length=50)),
                ('symptoms', models.ManyToManyField(related_name='health_data', to='symptom_checker.symptom')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('health_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_training.healthdata')),
            ],
        ),
    ]
