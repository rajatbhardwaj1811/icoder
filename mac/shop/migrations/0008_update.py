# Generated by Django 3.1.7 on 2021-03-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210313_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('order_update', models.CharField(max_length=500)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
