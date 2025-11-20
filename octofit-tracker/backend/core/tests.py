from django.test import TestCase
from .models import AppUser, Team, Activity, Workout, Leaderboard, Example

class ModelSmokeTest(TestCase):
	def test_create_appuser(self):
		user = AppUser.objects.create(email='test@example.com', name='Test User')
		self.assertEqual(user.email, 'test@example.com')

	def test_create_team(self):
		team = Team.objects.create(name='Marvel', description='Superhero team')
		self.assertEqual(team.name, 'Marvel')

	def test_create_activity(self):
		user = AppUser.objects.create(email='a@b.com', name='A')
		activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-01-01')
		self.assertEqual(activity.type, 'Run')

	def test_create_workout(self):
		workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
		self.assertEqual(workout.name, 'Pushups')

	def test_create_leaderboard(self):
		user = AppUser.objects.create(email='b@c.com', name='B')
		lb = Leaderboard.objects.create(user=user, score=100, rank=1)
		self.assertEqual(lb.rank, 1)
