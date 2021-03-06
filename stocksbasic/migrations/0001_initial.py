# Generated by Django 2.2.1 on 2020-05-01 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note_text', models.TextField(blank=True)),
                ('submition_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('updater', models.CharField(choices=[('IBO', 'IDAN'), ('SEF', 'Sefi')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exchange', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stocksbasic.Exchange')),
                ('notes', models.ManyToManyField(blank=True, to='stocksbasic.Note')),
            ],
        ),
    ]
