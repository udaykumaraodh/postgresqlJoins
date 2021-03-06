# Generated by Django 3.2.6 on 2021-08-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeModel',
            fields=[
                ('cname', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('c_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('d_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.collegemodel')),
            ],
        ),
        migrations.CreateModel(
            name='LecturerModel',
            fields=[
                ('lecturer_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('l_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.collegemodel')),
                ('depname', models.ManyToManyField(to='app1.DepartmentModel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('s_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.collegemodel')),
                ('dep', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.departmentmodel')),
                ('lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lecturermodel')),
            ],
        ),
    ]
