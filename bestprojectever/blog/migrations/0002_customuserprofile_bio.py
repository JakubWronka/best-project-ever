# Generated by Django 4.0.3 on 2022-04-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
