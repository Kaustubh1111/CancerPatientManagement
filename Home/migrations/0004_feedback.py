# Generated by Django 3.1 on 2021-03-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_physio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
    ]