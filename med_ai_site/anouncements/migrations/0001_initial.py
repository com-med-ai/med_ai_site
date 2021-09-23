# Generated by Django 3.2.7 on 2021-09-23 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField(max_length=128)),
                ('text', models.TextField(max_length=4096)),
                ('publication_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AnonuncemntPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Resim')),
                ('anouncement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anouncements.anouncements')),
            ],
        ),
    ]