# Generated by Django 3.0.4 on 2020-03-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200305_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='no',
        ),
        migrations.AlterField(
            model_name='posts',
            name='postid',
            field=models.IntegerField(db_column='POSTID', max_length=30, primary_key=True, serialize=False),
        ),
    ]