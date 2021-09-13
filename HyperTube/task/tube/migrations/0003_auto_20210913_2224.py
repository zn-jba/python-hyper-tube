# Generated by Django 2.2 on 2021-09-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20210913_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='tube.Tag'),
        ),
        migrations.AlterField(
            model_name='videotag',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='tube.Video'),
        ),
    ]
