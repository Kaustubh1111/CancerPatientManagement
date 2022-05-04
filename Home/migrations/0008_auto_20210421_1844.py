# Generated by Django 3.1 on 2021-04-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20210421_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_fname', models.CharField(max_length=20)),
                ('d_lname', models.CharField(max_length=20)),
                ('d_email', models.EmailField(max_length=20)),
                ('d_pwd', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]