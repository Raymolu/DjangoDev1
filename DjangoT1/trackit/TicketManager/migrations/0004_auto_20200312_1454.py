# Generated by Django 2.2.5 on 2020-03-12 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketManager', '0003_auto_20200312_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='status',
            new_name='status1',
        ),
    ]
