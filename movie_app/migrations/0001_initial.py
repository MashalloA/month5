# Generated by Django 5.1.4 on 2025-01-04 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Autor's Name")),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Movie Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Movie Description')),
                ('duration', models.IntegerField(default=0, verbose_name='Movie Duration')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.director', verbose_name="Autor's name")),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Review')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.movie')),
            ],
        ),
    ]
