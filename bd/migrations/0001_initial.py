# Generated by Django 4.2.2 on 2023-07-08 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaca_id', models.IntegerField()),
                ('data_nascimento_B', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=120)),
                ('senha', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vaca', models.CharField(max_length=30, verbose_name='NOME:')),
                ('raca', models.CharField(max_length=100)),
                ('lote', models.CharField(max_length=22)),
                ('numero_v', models.CharField(max_length=52, unique=True)),
                ('origem', models.CharField(max_length=200, null=True)),
                ('data_nascimento', models.DateField()),
                ('statu', models.CharField(choices=[('parida', 'Parida'), ('solteira', 'Solteira'), ('no_cio', 'No cio'), ('inseminada', 'Inseminada'), ('prenha', 'Prenha')], max_length=14)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reprodutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_reprodutor', models.CharField(max_length=100, null=True)),
                ('numero_r', models.CharField(max_length=22, unique=True)),
                ('raca', models.CharField(max_length=100)),
                ('lote', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('origem', models.CharField(max_length=200, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bd.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Bezerro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bezerro', models.CharField(max_length=120, null=True)),
                ('numero_b', models.CharField(max_length=22, unique=True)),
                ('raca', models.CharField(max_length=100)),
                ('lote', models.CharField(max_length=150)),
                ('origem', models.CharField(max_length=200, null=True)),
                ('data_nascimento', models.DateField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bd.usuario')),
            ],
        ),
    ]
