# Generated by Django 2.2.5 on 2020-03-06 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('MTL', 'Montreal'), ('LAV', 'Laval'), ('OTT', 'Ottawa'), ('TOK', 'Tokyo')], max_length=10)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
                ('penpal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=50)),
                ('review_comment', models.TextField(max_length=150)),
                ('stars', models.CharField(choices=[(1, 'one star'), (2, 'two stars'), (3, 'three stars'), (4, 'four stars'), (5, 'five stars')], max_length=10)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('validated_review', models.BooleanField(default=False)),
                ('Letter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviews', to='bloger.Letter')),
            ],
        ),
    ]
