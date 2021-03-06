# Generated by Django 4.0.4 on 2022-04-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSpotify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('artista', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('fechaDeNacimiento', models.DateField()),
                ('relacion', models.CharField(max_length=40)),
                ('generosFavoritos', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Cancion',
        ),
        migrations.DeleteModel(
            name='Podcast',
        ),
        migrations.RenameField(
            model_name='favoritos',
            old_name='tipo',
            new_name='album',
        ),
    ]
