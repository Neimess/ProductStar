# Generated by Django 4.2.5 on 2023-09-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
