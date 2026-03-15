from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class TeamTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam', members=['a@b.com'])
        self.assertEqual(team.name, 'TestTeam')

class ActivityTestCase(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='a@b.com', type='run', duration=10)
        self.assertEqual(activity.type, 'run')

class LeaderboardTestCase(TestCase):
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='TestTeam', points=50)
        self.assertEqual(lb.points, 50)

class WorkoutTestCase(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc')
        self.assertEqual(workout.name, 'TestWorkout')
