# Generated by Django 3.0.6 on 2020-07-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200728_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=384000)),
                ('result', models.IntegerField()),
            ],
        ),
    ]
