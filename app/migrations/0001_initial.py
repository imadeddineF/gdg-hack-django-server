# Generated by Django 4.0 on 2024-02-09 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('discord_id', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('number_of_outputs', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deliverables',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('submissions_deadline', models.DateTimeField()),
                ('judge_password', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')])),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge', to='app.event')),
                ('event_Feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge', to='app.feedback')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentor', to='app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Outputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coefficient', models.PositiveSmallIntegerField(default=1)),
                ('challenges', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='app.challenges')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='app.event')),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='app.deliverables')),
                ('processed_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outputs', to='app.occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant', to='app.event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant', to='app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team', to='app.event')),
            ],
            options={
                'unique_together': {('event', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='admin', serialize=False, to='app.profile')),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TotalResult',
            fields=[
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='total_result', serialize=False, to='app.team')),
                ('rate', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='winner', serialize=False, to='app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submission', to='app.event')),
                ('outputs', models.ManyToManyField(related_name='output_submission', to='app.Outputs')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submission', to='app.team')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantMentorFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant_feedback_to_mentor', to='app.feedback')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant_feedback_to_mentor', to='app.mentor')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant_feedback_to_mentor', to='app.participant')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantEventFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant_feedback_to_event', to='app.feedback')),
                ('event_Feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant_feedback_to_event', to='app.event')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participant', to='app.team'),
        ),
        migrations.CreateModel(
            name='OutputResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('comment', models.TextField()),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='output_result', to='app.outputs')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='output_result', to='app.team')),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentor', to='app.occupation'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentor', to='app.profile'),
        ),
        migrations.CreateModel(
            name='JudgeEventFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_Feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge_feedback_to_event', to='app.event')),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge_feedback_to_event', to='app.feedback')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge_feedback_to_event', to='app.judge')),
            ],
        ),
        migrations.AddField(
            model_name='judge',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge', to='app.occupation'),
        ),
        migrations.AddField(
            model_name='judge',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='judge', to='app.profile'),
        ),
        migrations.AddField(
            model_name='challenges',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='challenges', to='app.event'),
        ),
    ]
