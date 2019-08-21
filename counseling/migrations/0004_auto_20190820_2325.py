# Generated by Django 2.2.4 on 2019-08-20 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counseling', '0003_auto_20190820_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='counselor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Counselor'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Student'),
        ),
        migrations.AlterField(
            model_name='session',
            name='counselor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Counselor'),
        ),
        migrations.AlterField(
            model_name='session',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='portfolio.Student'),
        ),
    ]
