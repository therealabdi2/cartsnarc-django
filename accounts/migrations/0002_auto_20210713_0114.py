# Generated by Django 3.2.5 on 2021-07-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]
