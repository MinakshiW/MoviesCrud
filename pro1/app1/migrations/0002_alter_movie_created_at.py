# Generated by Django 5.0.7 on 2024-08-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
