# Generated by Django 2.2.4 on 2019-08-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_income',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='father_nric_no',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='father_race',
            field=models.CharField(choices=[('MALAY', 'MALAY'), ('CHINESE', 'CHINESE'), ('INDIAN', 'INDIAN'), ('OTHERS', 'OTHERS')], default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='father_religion',
            field=models.CharField(choices=[('ISLAM', 'ISLAM'), ('BUDDHA', 'BUDDHA'), ('CHRISTIAN', 'CHRISTIAN'), ('HINDU', 'HINDU'), ('OTHERS', 'OTHERS')], default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mother_income',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mother_nric_no',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mother_race',
            field=models.CharField(choices=[('MALAY', 'MALAY'), ('CHINESE', 'CHINESE'), ('INDIAN', 'INDIAN'), ('OTHERS', 'OTHERS')], default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mother_religion',
            field=models.CharField(choices=[('ISLAM', 'ISLAM'), ('BUDDHA', 'BUDDHA'), ('CHRISTIAN', 'CHRISTIAN'), ('HINDU', 'HINDU'), ('OTHERS', 'OTHERS')], default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='race',
            field=models.CharField(choices=[('MALAY', 'MALAY'), ('CHINESE', 'CHINESE'), ('INDIAN', 'INDIAN'), ('OTHERS', 'OTHERS')], default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('ISLAM', 'ISLAM'), ('BUDDHA', 'BUDDHA'), ('CHRISTIAN', 'CHRISTIAN'), ('HINDU', 'HINDU'), ('OTHERS', 'OTHERS')], default='', max_length=60),
            preserve_default=False,
        ),
    ]
