# Generated by Django 2.1.7 on 2019-05-21 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('college', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('counseller', models.CharField(blank=True, default='Dipendra KM', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('batch', models.CharField(choices=[('2018', 2018), ('2019', 2019)], default=2019, max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='admission',
            name='course_enrolled',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Course'),
        ),
        migrations.AddField(
            model_name='admission',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Group'),
        ),
    ]