# Generated by Django 2.1.5 on 2019-02-08 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionario", "0002_auto_20190208_0006"),
        ("hora_extra", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="horaextra",
            name="funcionario",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="funcionario.Funcionario",
            ),
            preserve_default=False,
        ),
    ]
