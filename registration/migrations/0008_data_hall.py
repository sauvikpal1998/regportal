# Generated by Django 2.0.6 on 2018-11-30 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regdesk', '0002_hall_gender'),
        ('registration', '0007_contingent_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Hall',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regdesk.Hall'),
        ),
    ]
