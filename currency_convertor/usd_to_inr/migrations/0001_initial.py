# Generated by Django 4.1.4 on 2023-03-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GDP_IN_US_dollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('gdp_usd', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
