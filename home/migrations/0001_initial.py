# Generated by Django 3.2.4 on 2021-07-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=50)),
                ('uemail', models.EmailField(max_length=50)),
                ('upassword', models.CharField(max_length=100)),
                ('uphone', models.IntegerField()),
                ('uviews', models.CharField(max_length=200)),
            ],
        ),
    ]
