# Generated by Django 4.2.1 on 2023-06-16 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.musician')),
            ],
        ),
    ]
