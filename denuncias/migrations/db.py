from django.db import migrations, models
class Migration (migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'Denuncia',
            fields=[
               ('id', models.AutoField(auto_created=True,
                                       primary_key=True, serialize=False, verbose_name='ID')),
               ('cpf',  models.CharField(max_length=100)),
               ('depoimento',  models.CharField(max_length=500)),
               ('empresa',  models.CharField(max_length=100)),
               ('local',  models.CharField(max_length=100)),
               ('hora',  models.CharField(max_length=100)),
            ],
        ),
    ]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name= 'Tipo',
            fields = [
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('trabalho_escravo', models.CharField(max_length=100)),
                ('assedio', models.CharField(max_length=100)),
                ('discriminacao', models.CharField(max_length=100)),
                ('outros', models.CharField(max_length=100)),
            ]
        )
    ]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('data_de_nascimento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
            ]
        )
    ]