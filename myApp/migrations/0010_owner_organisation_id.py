# Generated by Django 4.2.6 on 2024-05-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_recycleform'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='organisation_id',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
