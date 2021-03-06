# Generated by Django 3.0.7 on 2020-06-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, upload_to='profile/')),
                ('bio', models.CharField(max_length=30)),
                ('userId', models.IntegerField()),
            ],
            options={
                'ordering': ['pic'],
            },
        ),
    ]
