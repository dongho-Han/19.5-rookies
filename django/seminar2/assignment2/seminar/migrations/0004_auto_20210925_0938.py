# Generated by Django 3.2.6 on 2021-09-25 09:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seminar', '0003_auto_20210925_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='capacity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seminar',
            name='count',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seminar',
            name='online',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='time',
            field=models.TimeField(default=datetime.time(9, 38, 6, 429397)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participantprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userseminar',
            name='seminar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_seminars', to='seminar.seminar'),
        ),
        migrations.AlterField(
            model_name='userseminar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_seminars', to=settings.AUTH_USER_MODEL),
        ),
    ]
