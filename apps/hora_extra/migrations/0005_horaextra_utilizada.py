# Generated by Django 2.1.1 on 2020-02-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hora_extra', '0004_horaextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]