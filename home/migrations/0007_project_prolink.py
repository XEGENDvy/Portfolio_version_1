# Generated by Django 4.2.2 on 2023-10-10 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prolink',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
