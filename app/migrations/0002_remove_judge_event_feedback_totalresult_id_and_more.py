# Generated by Django 4.0 on 2024-02-09 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='event_Feedback',
        ),
        migrations.AddField(
            model_name='totalresult',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='admin', serialize=False, to='app.profile'),
        ),
        migrations.AlterField(
            model_name='totalresult',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='total_result', to='app.team'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='winner', serialize=False, to='app.team'),
        ),
    ]