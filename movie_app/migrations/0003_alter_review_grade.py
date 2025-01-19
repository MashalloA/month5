# Generated by Django 5.1.4 on 2025-01-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='*', max_length=10, null=True, verbose_name='Grade'),
        ),
    ]
