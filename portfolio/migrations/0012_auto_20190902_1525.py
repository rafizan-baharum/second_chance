# Generated by Django 2.2.4 on 2019-09-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_school_contact_person'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-modified_date'], 'verbose_name_plural': 'Students'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='registered_date',
        ),
    ]