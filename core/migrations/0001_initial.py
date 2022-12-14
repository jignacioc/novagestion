# Generated by Django 4.1 on 2022-11-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutJefeFamilia', models.CharField(max_length=9, verbose_name='Rut Jefe Familia: ')),
                ('numIntegrantes', models.IntegerField(verbose_name='N° de integrantes: ')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección Hogar: ')),
                ('antecedentes', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]
