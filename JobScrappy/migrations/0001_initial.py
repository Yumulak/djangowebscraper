# Generated by Django 4.2.1 on 2023-05-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Display Name')),
                ('email', models.EmailField(max_length=254)),
                ('urllist', models.CharField(max_length=1000, verbose_name='URL')),
                ('interval', models.CharField(choices=[('1', 'daily'), ('2', 'weekly'), ('3', 'monthly')], max_length=10)),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
    ]