# Generated by Django 5.0.6 on 2024-06-09 16:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0003_remove_symptomchecker_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptomchecker',
            old_name='additional_information',
            new_name='Symptom_History',
        ),
        migrations.RemoveField(
            model_name='symptomchecker',
            name='gender',
        ),
        migrations.AddField(
            model_name='symptomchecker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='symptomchecker',
            name='duration',
            field=models.CharField(choices=[('H', 'Hours'), ('D', 'Days'), ('M', 'Months'), ('Y', 'Years')], max_length=1),
        ),
        migrations.AlterField(
            model_name='symptomchecker',
            name='severity',
            field=models.CharField(choices=[('M', 'Mild'), ('MO', 'Moderate'), ('S', 'Severe')], max_length=2),
        ),
    ]