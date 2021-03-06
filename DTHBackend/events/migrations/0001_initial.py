# Generated by Django 3.0.8 on 2020-11-27 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_apply', models.TextField(max_length=5000)),
                ('is_assessed', models.BooleanField()),
                ('is_accepted', models.BooleanField()),
                ('apply_keynote', models.BooleanField()),
                ('apply_facilitator', models.BooleanField()),
                ('apply_mentor', models.BooleanField()),
                ('apply_expert', models.BooleanField()),
                ('apply_enthusiast', models.BooleanField()),
                ('is_anon', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_description', models.TextField(max_length=5000)),
                ('event_location', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_ticket', models.CharField(max_length=200)),
                ('skills_keynote', models.BooleanField()),
                ('skills_facilitator', models.BooleanField()),
                ('skills_mentor', models.BooleanField()),
                ('skills_expert', models.BooleanField()),
                ('skills_enthusiast', models.BooleanField()),
                ('event_size', models.IntegerField(choices=[(1, 'Intimate'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Verylarge'), (6, 'Huge')])),
                ('is_paid', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2000)),
                ('rating', models.IntegerField(choices=[(1, 'Onestar'), (2, 'Twostars'), (3, 'Threestars'), (4, 'Fourstars'), (5, 'Fivestars')])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_event', to='events.Event')),
            ],
        ),
    ]
