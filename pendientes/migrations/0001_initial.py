# Generated by Django 4.0.5 on 2023-03-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pendientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Folio')),
                ('Area', models.CharField(choices=[('SubAdministrativa', 'SubAdministrativa'), ('SubPlaneacion', 'SubPlaneacion'), ('SubAcademica', 'SubAcademica')], max_length=30, verbose_name='Estado')),
                ('tarea', models.CharField(max_length=200, verbose_name='Pendiente')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Asignacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Conclusion')),
                ('estado', models.CharField(choices=[('Finalizada', 'Finalizada'), ('En Proceso', 'En Proceso'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=25, verbose_name='Estado')),
            ],
        ),
    ]
