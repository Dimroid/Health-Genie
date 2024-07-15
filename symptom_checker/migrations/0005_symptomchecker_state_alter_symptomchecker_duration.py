# Generated by Django 5.0.6 on 2024-06-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0004_rename_additional_information_symptomchecker_symptom_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptomchecker',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='symptomchecker',
            name='duration',
            field=models.CharField(choices=[('H', 'Hours'), ('D', 'Days'), ('W', 'Weeks'), ('M', 'Months'), ('Y', 'Years')], max_length=1),
        ),
    ]