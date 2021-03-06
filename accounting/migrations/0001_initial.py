# Generated by Django 2.1.7 on 2019-05-21 12:48

import accounting.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rupes', models.FloatField(validators=[accounting.models.is_positive])),
                ('checque', models.FileField(blank=True, null=True, upload_to='expenses/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpensesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rupes', models.FloatField(validators=[accounting.models.is_positive])),
                ('bill_no', models.CharField(blank=True, max_length=100, null=True)),
                ('biiling_file', models.FileField(blank=True, null=True, upload_to='income/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.IncomeCategory'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.ExpensesCategory'),
        ),
    ]
