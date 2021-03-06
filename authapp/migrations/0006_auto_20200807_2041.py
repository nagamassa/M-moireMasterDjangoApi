# Generated by Django 3.0.6 on 2020-08-07 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20200807_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='blocage',
        ),
        migrations.AddField(
            model_name='article',
            name='etat',
            field=models.CharField(choices=[('Préparation', 'Préparation'), ('Rejeté', 'Rejeté'), ('Accepté', 'Accepté'), ('En cours de traitement', 'En cours de traitement')], default='Préparation', max_length=30),
        ),
        migrations.CreateModel(
            name='Rejet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison', models.TextField()),
                ('dateRejet', models.DateTimeField(blank=True, null=True)),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloque', to='authapp.Article')),
                ('bloqueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueur', to='authapp.Agence')),
            ],
            options={
                'db_table': 'Rejet',
            },
        ),
        migrations.AddField(
            model_name='agence',
            name='bloques',
            field=models.ManyToManyField(through='authapp.Rejet', to='authapp.Article'),
        ),
        migrations.AddConstraint(
            model_name='rejet',
            constraint=models.UniqueConstraint(fields=('bloqueur', 'bloque'), name='unique_rejet'),
        ),
    ]
