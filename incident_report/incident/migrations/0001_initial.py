# Generated by Django 3.2.5 on 2021-07-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=100)),
                ('Position', models.IntegerField()),
                ('User', models.CharField(max_length=100)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]