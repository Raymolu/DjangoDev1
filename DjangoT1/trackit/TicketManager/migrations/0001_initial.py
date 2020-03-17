# Generated by Django 2.2.5 on 2020-03-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('tracking_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(choices=[('FirstWood', 'FirstWood'), ('LumberExport', 'LumberExport'), ('JackInTheBox', 'JackInTheBox'), ('BigWood Inc.', 'BigWood Inc.'), ('', 'other')], max_length=25)),
                ('contact', models.CharField(max_length=25)),
                ('agent', models.CharField(choices=[('Ludovic Raymond', 'Ludovic'), ('Jean Beauce', 'Jean'), ('Tobby Love', 'Tobby')], max_length=25)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('close', 'Close'), ('stand_by', 'Stand by')], max_length=15)),
                ('startDate', models.DateField(auto_now_add=True)),
                ('endDate', models.DateField()),
            ],
        ),
    ]