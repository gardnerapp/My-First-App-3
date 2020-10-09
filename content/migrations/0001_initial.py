# Generated by Django 3.0.4 on 2020-03-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('essay', models.FileField(blank=True, null=True, upload_to='essays')),
                ('pub_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
