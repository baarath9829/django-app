# Generated by Django 3.0.3 on 2020-08-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('derma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
