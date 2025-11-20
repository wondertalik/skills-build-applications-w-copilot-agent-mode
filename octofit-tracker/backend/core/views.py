from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import AppUser, Team, Activity, Workout, Leaderboard, Example
from .serializers import AppUserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer, ExampleSerializer

class AppUserViewSet(viewsets.ModelViewSet):
	queryset = AppUser.objects.all()
	serializer_class = AppUserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

class ExampleViewSet(viewsets.ModelViewSet):
	queryset = Example.objects.all()
	serializer_class = ExampleSerializer
