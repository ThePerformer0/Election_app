# Generated by Django 4.2.17 on 2025-02-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_rename_annee_candidature_etudiant_annee_scolaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='candidats_photos/'),
        ),
    ]
