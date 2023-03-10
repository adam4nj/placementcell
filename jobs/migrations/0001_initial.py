# Generated by Django 4.1.3 on 2023-02-19 13:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=20)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_date', models.DateField()),
                ('salary', models.PositiveIntegerField(max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Accepted'), ('1', 'Pending'), ('2', 'Rejected')], default='1', max_length=1)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
