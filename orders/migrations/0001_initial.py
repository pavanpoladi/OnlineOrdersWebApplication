# Generated by Django 2.0.3 on 2020-06-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfFood', models.CharField(max_length=64)),
                ('flavor', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('price', models.FloatField()),
            ],
        ),
    ]
