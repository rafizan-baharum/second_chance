# Generated by Django 2.2.4 on 2019-08-22 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financialaid', '0007_grant_purpose'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grant',
            options={'ordering': ['approved_date']},
        ),
    ]