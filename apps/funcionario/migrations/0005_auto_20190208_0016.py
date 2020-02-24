# Generated by Django 2.1.5 on 2019-02-08 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionario", "0004_auto_20190208_0015"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="departamento",
            field=models.ManyToManyField(to="departamento.Departamento"),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="empresa.Empresa"
            ),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
