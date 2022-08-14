# Generated by Django 4.0.5 on 2022-07-03 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('end', models.DateTimeField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deescription', models.TextField(blank=True, default='')),
                ('status', models.SmallIntegerField(choices=[(1, 'Not started'), (2, 'In progress'), (3, 'Testing'), (4, 'Done')], default=1)),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('due', models.DateTimeField(blank=True, null=True)),
                ('complete', models.DateTimeField(blank=True, null=True)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.sprint')),
            ],
        ),
    ]
