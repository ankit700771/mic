# Generated by Django 3.0.6 on 2020-07-27 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_admission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='lop',
            new_name='lor',
        ),
    ]
