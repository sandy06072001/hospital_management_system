# Generated by Django 4.1.7 on 2023-03-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_patient_prescription_remove_patient_symptoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
