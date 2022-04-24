# Generated by Django 4.0.3 on 2022-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('ProjectID', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=100)),
                ('ProjectBeginning', models.DateField()),
                ('ProjectEnd', models.DateField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Risk', models.IntegerField()),
                ('Participants', models.TextField()),
            ],
        ),
    ]