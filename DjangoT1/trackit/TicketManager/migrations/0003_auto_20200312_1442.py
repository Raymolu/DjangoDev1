# Generated by Django 2.2.5 on 2020-03-12 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketManager', '0002_auto_20200312_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='endDate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='startDate',
            new_name='start_date',
        ),
    ]
