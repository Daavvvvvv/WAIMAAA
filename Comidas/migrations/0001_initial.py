# Generated by Django 4.0.6 on 2023-05-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=5000)),
                ('peso', models.IntegerField(max_length=100)),
                ('informacion', models.TextField(max_length=4000)),
            ],
        ),
    ]
