# Generated by Django 4.2.2 on 2023-06-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.CharField(max_length=12),
        ),
    ]
