# Generated by Django 3.0.6 on 2020-08-07 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20200724_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textalertesugession',
            name='auteur',
        ),
        migrations.DeleteModel(
            name='TextAlerte',
        ),
        migrations.DeleteModel(
            name='TextAlerteSugession',
        ),
    ]