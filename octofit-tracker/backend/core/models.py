
from django.db import models

# Example model for demonstration
class Example(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

# User model (for demonstration, not replacing Django's auth.User)
class AppUser(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	team = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.email

# Team model
class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name

# Activity model
class Activity(models.Model):
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	type = models.CharField(max_length=100)
	duration = models.PositiveIntegerField(help_text="Duration in minutes")
	date = models.DateField()
	def __str__(self):
		return f"{self.user.email} - {self.type}"

# Workout model
class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name

# Leaderboard model
class Leaderboard(models.Model):
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	score = models.IntegerField()
	rank = models.PositiveIntegerField()
	def __str__(self):
		return f"{self.user.email} - Rank {self.rank}"
