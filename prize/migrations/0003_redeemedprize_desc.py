# Generated by Django 4.1 on 2022-10-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prize', '0002_alter_redeemedprize_nama'),
    ]

    operations = [
        migrations.AddField(
            model_name='redeemedprize',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
