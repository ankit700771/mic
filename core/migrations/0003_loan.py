# Generated by Django 3.0.6 on 2020-07-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=6)),
                ('married', models.CharField(max_length=3)),
                ('dependents', models.IntegerField()),
                ('education', models.CharField(max_length=12)),
                ('self_employed', models.CharField(max_length=3)),
                ('applicant_income', models.IntegerField()),
                ('co_applicant_income', models.IntegerField()),
                ('loan_amount', models.IntegerField()),
                ('loan_amount_term', models.IntegerField()),
                ('credit_history', models.IntegerField()),
                ('property_area', models.CharField(max_length=5)),
                ('result', models.CharField(max_length=1)),
            ],
        ),
    ]