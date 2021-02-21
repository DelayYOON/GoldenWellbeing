# Generated by Django 3.1.6 on 2021-02-20 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='lecture_videos')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='lectures.lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]