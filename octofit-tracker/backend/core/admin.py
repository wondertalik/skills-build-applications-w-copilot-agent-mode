
from django.contrib import admin
from .models import Example, AppUser, Team, Activity, Workout, Leaderboard

admin.site.register(Example)
admin.site.register(AppUser)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
