# Generated by Django 2.1.5 on 2019-02-08 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0003_auto_20190208_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='funcionario.Funcionario'),
        ),
    ]
