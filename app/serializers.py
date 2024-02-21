from .models import *
from rest_framework import serializers

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)

class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=16)

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class DeliverablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverables
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

class ChallengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outputs
        fields = '__all__'

class TeamRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRegistration
        fields = '__all__'

class TeamAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRegistration
        fields = ['id']

class ParticipantRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantRegistration
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class RequestMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestMentor
        fields = '__all__'

class WebsiteSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteSession
        fields = ['event']
        extra_kwargs = {
            'event': {
                'validators': []
            }
        }

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'