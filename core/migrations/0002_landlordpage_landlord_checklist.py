# Generated by Django 4.1.5 on 2023-01-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlordpage',
            name='landlord_checklist',
            field=models.TextField(default=1, verbose_name='LandLord CheckList'),
            preserve_default=False,
        ),
    ]
