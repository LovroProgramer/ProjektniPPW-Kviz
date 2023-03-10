# Generated by Django 4.1.4 on 2022-12-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kviz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeKviza', models.CharField(max_length=100)),
                ('tezina', models.IntegerField()),
                ('kategorija', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Odgovori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('tocanOdg', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('ime', models.CharField(max_length=20)),
                ('prezime', models.CharField(max_length=20)),
                ('pitanjeOdg2', models.IntegerField()),
                ('PrijavljenaZaKviz', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.kviz')),
            ],
        ),
        migrations.CreateModel(
            name='Pitanja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('kategorija', models.CharField(max_length=100)),
                ('imeKviza', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.kviz')),
                ('text', models.ManyToManyField(to='main.odgovori')),
            ],
        ),
    ]
