# Generated by Django 5.0.2 on 2024-03-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_medico_mail_remove_paciente_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='mail',
            field=models.EmailField(default='.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='mail',
            field=models.EmailField(default='.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recetas',
            name='codigo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
