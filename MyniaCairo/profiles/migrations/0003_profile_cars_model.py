# Generated by Django 2.2.4 on 2019-08-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cars_model',
            field=models.CharField(blank=True, choices=[('1', 'فيات'), ('2', 'مرسيدس'), ('3', 'بي ام دابليو'), ('4', 'دايو'), ('5', 'متسوبيشي'), ('6', 'كيا'), ('7', 'تيوتا'), ('8', 'بيجو'), ('9', 'أخري')], max_length=20, null=True),
        ),
    ]
