# Generated by Django 4.1 on 2022-11-08 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostularPrograma',
            fields=[
                ('id_postulacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAlumno', models.CharField(max_length=70, verbose_name='Nombre del alumno: ')),
                ('emailAlumno', models.EmailField(max_length=70, verbose_name='Email del alumno: ')),
                ('motivoPostulacion', models.CharField(max_length=70, verbose_name='Motivo de la postulación: ')),
                ('id_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.programa')),
            ],
        ),
    ]
