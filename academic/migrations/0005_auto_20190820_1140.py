# Generated by Django 2.2.4 on 2019-08-20 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20190820_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='parent',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results', to='academic.Resultbook'),
        ),
    ]
