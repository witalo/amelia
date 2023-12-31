# Generated by Django 4.2.6 on 2023-10-10 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad')),
                ('old_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad Anterior')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('V', 'VENTA'), ('C', 'COMPRA'), ('M', 'EMPEÑO'), ('R', 'ENTREGA'), ('E', 'ENTRADA'), ('S', 'SALIDA')], default='V', max_length=1, verbose_name='TIPO')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='CORRELATIVO')),
                ('status', models.CharField(choices=[('C', 'COMPLETADO'), ('P', 'PENDIENTE'), ('A', 'ANULADO')], default='P', max_length=1, verbose_name='ESTADO')),
                ('init', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('current', models.DateField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('relative', models.IntegerField(default=0, verbose_name='ORDER RELACIONAL')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client', verbose_name='CLIENTE')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='providers.provider', verbose_name='PROVEEDOR')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'ordering': ['id'],
            },
        ),
    ]
