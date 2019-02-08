# Generated by Django 2.1.5 on 2019-02-08 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='nome',
            new_name='descricao',
        ),
        migrations.AddField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.Funcionario'),
        ),
    ]
