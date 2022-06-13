# Generated by Django 4.0.3 on 2022-06-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('img', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Days', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.city')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobtitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('National_num', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=100)),
                ('BirthDay', models.DateTimeField()),
                ('Phone', models.CharField(max_length=11)),
                ('reserved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.city')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('startdate', models.DateTimeField(null=True)),
                ('enddate', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('Doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.doctor')),
                ('Pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.patient')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=100)),
                ('PatientDoctor', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Disease', models.CharField(max_length=100)),
                ('State_of_treatement', models.BooleanField(default=False)),
                ('have', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Admin.patient')),
                ('write', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Admin.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_Id', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
            ],
        ),
    ]