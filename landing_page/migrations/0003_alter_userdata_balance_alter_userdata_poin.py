# Generated by Django 4.1 on 2022-10-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_alter_userdata_balance_alter_userdata_poin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='poin',
            field=models.BigIntegerField(default=0),
        ),
    ]
