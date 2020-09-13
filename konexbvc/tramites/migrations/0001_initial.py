# Generated by Django 3.1.1 on 2020-09-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=300)),
                ('tramite', models.CharField(choices=[('DONACION', 'Donación'), ('SUCESION', 'Sucesión'), ('ACT_DATO', 'Actualización datos')], max_length=8)),
                ('comunicacion', models.CharField(choices=[('CORREO', 'Correo'), ('FISICO', 'Dirección Fisioa')], max_length=6)),
                ('solicitud', models.CharField(max_length=2000)),
                ('estado', models.CharField(choices=[('REGISTRADO', 'Registrado'), ('ASESOR', 'Asignado a un asesor'), ('TECNICO', 'Asignado a un soporte técnico'), ('SOLUCIONADO', 'Solucionado')], max_length=11)),
            ],
        ),
    ]
