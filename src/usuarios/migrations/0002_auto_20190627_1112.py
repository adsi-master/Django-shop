# Generated by Django 2.1.8 on 2019-06-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioparametros',
            name='tipodocumento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuarios.TipoDocumento'),
        ),
    ]
