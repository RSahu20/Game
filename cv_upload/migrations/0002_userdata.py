# Generated by Django 5.0.6 on 2024-05-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('credit_score', models.IntegerField()),
                ('credit_lines', models.IntegerField()),
                ('masked_phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
