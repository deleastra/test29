# Generated by Django 2.0.3 on 2018-03-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.BooleanField()),
                ('correct', models.IntegerField(default=0)),
                ('incorrect', models.IntegerField(default=0)),
            ],
        ),
    ]
