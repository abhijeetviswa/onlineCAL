# Generated by Django 3.0.2 on 2020-12-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_portal', '0004_userdetail_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='status',
            field=models.BooleanField(default=True, help_text='Will cancel all slot of this instrument', verbose_name='Current Status'),
        ),
    ]
