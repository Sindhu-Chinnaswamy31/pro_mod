# Generated by Django 3.0 on 2020-09-16 14:08

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200916_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[myapp.models.validate_name])),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
    ]
