# Generated by Django 4.2.6 on 2023-10-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('document', models.CharField(default='', max_length=15, unique=True)),
                ('phone', models.CharField(blank=True, max_length=9, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('is_state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
    ]
