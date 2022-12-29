from rest_framework import serializers
from callretriver.models import Company, Team, User, Call


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['name', 'company_parent']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['name', 'company_parent', 'team_parent']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'company_parent', 'team_parent']


class CallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Call
        fields = ['owner', 'data']
