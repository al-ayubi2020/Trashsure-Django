# Generated by Django 4.1 on 2022-10-28 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_alter_userdata_balance_alter_userdata_poin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
