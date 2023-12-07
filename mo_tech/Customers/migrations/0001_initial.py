# Generated by Django 4.2 on 2023-12-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustumersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.CharField(max_length=60)),
                ('status', models.SmallIntegerField(default=1)),
                ('score', models.DecimalField(decimal_places=10, default=0.0, max_digits=20)),
                ('preapproved_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'customers_customer',
            },
        ),
    ]
