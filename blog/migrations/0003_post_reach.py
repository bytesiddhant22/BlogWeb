# Generated by Django 5.0.7 on 2024-08-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reach',
            field=models.CharField(choices=[('featured', 'Featured'), ('normal', 'Normal')], default='normal', max_length=20),
        ),
    ]
