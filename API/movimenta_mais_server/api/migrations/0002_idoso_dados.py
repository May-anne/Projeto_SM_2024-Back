# Generated by Django 5.0.4 on 2024-07-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idoso_Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('raca', models.CharField(max_length=20)),
                ('escolaridade', models.CharField(max_length=50)),
                ('deficiencia', models.BooleanField()),
                ('deficiencia_quais', models.TextField(max_length=500)),
                ('telefone_pessoal', models.CharField(max_length=11)),
                ('telefone_emergencial', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=8)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('cartao_cns', models.CharField(max_length=15)),
                ('plano_saude', models.BooleanField()),
                ('plano_saude_qual', models.CharField(blank=True, max_length=50, null=True)),
                ('onde_moras', models.CharField(max_length=50)),
                ('com_quem_mora', models.TextField(max_length=200)),
                ('quantos_residem', models.PositiveSmallIntegerField()),
                ('meio_transporte', models.CharField(max_length=50)),
                ('situacao_economica', models.CharField(max_length=50)),
                ('renda', models.IntegerField()),
                ('problemas_saude', models.BooleanField()),
                ('problemas_saude_quais', models.TextField(blank=True, max_length=500, null=True)),
                ('cirgurgia_recente', models.BooleanField()),
                ('cirurgia_quais', models.TextField(blank=True, max_length=500, null=True)),
                ('internacao_recente', models.BooleanField()),
                ('internacao_quais', models.TextField(blank=True, max_length=500, null=True)),
                ('alcool', models.BooleanField()),
                ('fumante', models.BooleanField()),
                ('drogas', models.BooleanField()),
                ('medicamentos', models.BooleanField()),
                ('medicamentos_quais', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
