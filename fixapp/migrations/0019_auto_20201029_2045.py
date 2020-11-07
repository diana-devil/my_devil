# Generated by Django 3.1.1 on 2020-10-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixapp', '0018_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='img',
        ),
        migrations.AddField(
            model_name='class_fix',
            name='photo',
            field=models.ImageField(default='user1.jpg', upload_to='ptotos'),
        ),
        migrations.AddField(
            model_name='class_fix',
            name='user',
            field=models.CharField(default='user1.jpg', max_length=100),
        ),
    ]