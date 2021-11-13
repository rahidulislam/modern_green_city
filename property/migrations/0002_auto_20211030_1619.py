# Generated by Django 3.2.8 on 2021-10-30 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='land_type/')),
            ],
        ),
        migrations.AddField(
            model_name='land',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='car_parking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='contact',
            field=models.CharField(default='0124', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='description',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='flat_area',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='land',
            name='land_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.landtype'),
        ),
    ]
