# Generated by Django 2.2.4 on 2019-08-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financialaid', '0004_grant_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
