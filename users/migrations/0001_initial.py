# Generated by Django 4.0.5 on 2022-06-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=20, unique=True, verbose_name='full Name')),
                ('phone', models.CharField(max_length=14, verbose_name='Mobile Number')),
                ('phone2', models.CharField(blank=True, max_length=14, verbose_name='Alternate Number')),
                ('address', models.CharField(max_length=60, null=True, verbose_name='Address')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
