# Generated by Django 3.0.4 on 2020-05-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subaruhelp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
