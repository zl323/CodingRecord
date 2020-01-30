# Generated by Django 3.0 on 2020-01-20 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_text', models.CharField(max_length=200)),
                ('num_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=200)),
                ('num_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Problem')),
            ],
        ),
    ]