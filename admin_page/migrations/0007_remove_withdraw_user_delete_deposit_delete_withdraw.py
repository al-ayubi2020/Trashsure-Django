# Generated by Django 4.1 on 2022-10-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0006_prize_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdraw',
            name='user',
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Withdraw',
        ),
    ]
