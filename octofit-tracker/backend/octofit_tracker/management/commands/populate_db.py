from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        marvel_users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com'),
        ]
        dc_users = [
            User.objects.create_user(username='batman', email='batman@dc.com'),
            User.objects.create_user(username='superman', email='superman@dc.com'),
        ]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', members=[u.email for u in marvel_users])
        dc_team = Team.objects.create(name='DC', members=[u.email for u in dc_users])

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30)
        Activity.objects.create(user_email='batman@dc.com', type='cycle', duration=45)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=80)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
