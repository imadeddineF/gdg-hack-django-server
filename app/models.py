from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import *

class Occupation(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Deliverables(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Feedback(models.Model):
    RATING_CHOICES = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    )

    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    discord_id = models.CharField(max_length=32, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_occupied = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'phone_number']

    objects = ProfileManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Admin(models.Model):
    profile = models.OneToOneField(Profile, related_name='admin', on_delete=models.PROTECT, primary_key=True)

class Event(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    submissions_deadline = models.DateTimeField()
    leader = models.ForeignKey(Profile, related_name='event', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

class TeamRegistration(models.Model):
    event = models.ForeignKey(Event, related_name='team_registration', on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    number_of_team = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('event', 'name')

class ParticipantRegistration(models.Model):
    motivation_letter = models.TextField()
    profile = models.ForeignKey(Profile, related_name='registration', on_delete=models.PROTECT)
    team = models.ForeignKey(TeamRegistration, related_name='registration', on_delete=models.PROTECT)
    occupation = models.ForeignKey(Occupation, related_name='registration', on_delete=models.PROTECT)

class Challenges(models.Model):
    event = models.ForeignKey(Event, related_name='challenges', on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    description = models.TextField()
    number_of_outputs = models.PositiveSmallIntegerField()

class Agenda(models.Model):
    event = models.ForeignKey(Event, related_name='agenda', on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    activity = models.CharField(max_length=20)

    class Meta:
        unique_together = ('event', 'date_time')

class Mentor(models.Model):
    profile = models.ForeignKey(Profile, related_name='mentor', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name='mentor', on_delete=models.PROTECT)
    occupation = models.ForeignKey(Occupation, related_name='mentor', on_delete=models.PROTECT)

class Judge(models.Model):
    profile = models.ForeignKey(Profile, related_name='judge', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name='judge', on_delete=models.PROTECT)
    occupation = models.ForeignKey(Occupation, related_name='judge', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('profile', 'event')

class JudgeEventFeedback(models.Model):
    event_Feedback = models.ForeignKey(Event, related_name='judge_feedback_to_event', on_delete=models.PROTECT)
    feedback = models.ForeignKey(Feedback, related_name='judge_feedback_to_event', on_delete=models.PROTECT)
    judge = models.ForeignKey(Judge, related_name='judge_feedback_to_event', on_delete=models.PROTECT)

class Team(models.Model):
    event = models.ForeignKey(Event, related_name='team', on_delete=models.PROTECT)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('event', 'name')

class Participant(models.Model):
    profile = models.ForeignKey(Profile, related_name='participant', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='participant', on_delete=models.PROTECT)

class ParticipantMentorFeedback(models.Model):
    mentor = models.ForeignKey(Mentor, related_name='participant_feedback_to_mentor', on_delete=models.PROTECT)
    participant = models.ForeignKey(Participant, related_name='participant_feedback_to_mentor', on_delete=models.PROTECT)
    feedback = models.ForeignKey(Feedback, related_name='participant_feedback_to_mentor', on_delete=models.PROTECT)

class ParticipantEventFeedback(models.Model):
    event_Feedback = models.ForeignKey(Event, related_name='participant_feedback_to_event', on_delete=models.PROTECT)
    Feedback = models.ForeignKey(Feedback, related_name='participant_feedback_to_event', on_delete=models.PROTECT)

class RequestMentor(models.Model):
    team = models.ForeignKey(Team, related_name='request_mentor', on_delete=models.PROTECT)
    mentor = models.ForeignKey(Mentor, related_name='request_mentor', on_delete=models.PROTECT)
    requested = models.DateTimeField(auto_now_add=True)

class WebsiteSession(models.Model):
    event = models.OneToOneField(Event, related_name='website_session', on_delete=models.PROTECT, primary_key=True)
    grant_to_judge = models.BooleanField(default=False)
    grant_to_participants = models.BooleanField(default=False)

class Outputs(models.Model):
    coefficient = models.PositiveSmallIntegerField(default=1)
    event = models.ForeignKey(Event, related_name='outputs', on_delete=models.PROTECT)
    output = models.ForeignKey(Deliverables, related_name='outputs', on_delete=models.PROTECT)
    challenges = models.ForeignKey(Challenges, related_name='outputs', on_delete=models.PROTECT)
    processed_by = models.ForeignKey(Occupation, related_name='outputs', on_delete=models.PROTECT)

class Submission(models.Model):
    event = models.ForeignKey(Event, related_name='submission', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='submission', on_delete=models.PROTECT)
    outputs = models.ManyToManyField(Outputs, related_name='output_submission')
    submitted = models.DateTimeField(auto_now_add=True)

class OutputResult(models.Model):
    team = models.ForeignKey(Team, related_name='output_result', on_delete=models.PROTECT)
    output = models.ForeignKey(Outputs, related_name='output_result', on_delete=models.PROTECT)
    rate = models.PositiveSmallIntegerField()
    comment = models.TextField()

class TotalResult(models.Model):
    team = models.OneToOneField(Team, related_name='total_result', on_delete=models.PROTECT, primary_key=True)
    rate = models.PositiveSmallIntegerField()

class Winner(models.Model):
    team = models.OneToOneField(Team, related_name='winner', on_delete=models.PROTECT, primary_key=True)