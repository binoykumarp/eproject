# Generated by Django 4.2.4 on 2023-09-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('profile', models.ImageField(upload_to='manager')),
            ],
        ),
    ]
