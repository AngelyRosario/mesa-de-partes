# Generated by Django 2.2.7 on 2019-11-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0009_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='descripcion',
            field=models.TextField(help_text='Descripción de lo que está ocurriendo en la imagen. Necesario para ser inclusivo con los estudiantes con visión limitada'),
        ),
    ]