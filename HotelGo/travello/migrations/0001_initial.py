# Generated by Django 4.2.1 on 2023-05-10 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('offer', models.BooleanField(default=False)),
                ('rate', models.IntegerField()),
                ('stars', models.IntegerField()),
                ('town', models.CharField()),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hotel_destination', to='travello.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfRoom', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'triple'), ('suite', 'Suite')], default=None, max_length=20)),
                ('availability', models.BooleanField()),
                ('price', models.IntegerField()),
                ('hotelRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rooms', to='travello.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='hotelImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='pics')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hotel_Images', to='travello.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.hotel')),
            ],
        ),
    ]
