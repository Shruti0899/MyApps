# Generated by Django 2.1.2 on 2018-10-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfirst_app', '0003_auto_20181009_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('psw', models.CharField(max_length=10)),
            ],
        ),
    ]