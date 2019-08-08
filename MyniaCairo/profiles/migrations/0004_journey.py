# Generated by Django 2.2.4 on 2019-08-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_cars_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_from', models.CharField(choices=[('1', 'المنيا'), ('2', 'القاهرة')], max_length=20)),
                ('journey_kind', models.CharField(choices=[('1', 'شير بنزين'), ('2', 'شركة سفريات')], max_length=20)),
                ('date', models.DateField()),
                ('start_range', models.TimeField()),
                ('available_places', models.IntegerField()),
                ('share_price', models.IntegerField()),
                ('travieler', models.ManyToManyField(to='profiles.Profile')),
            ],
        ),
    ]