# Generated by Django 3.1.6 on 2021-04-15 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grocerybag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('itemname', models.CharField(max_length=100, null=True)),
                ('itemquantity', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('NUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grocerybag.nuser')),
            ],
        ),
    ]
