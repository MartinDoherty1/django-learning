from django.contrib import admin

from gym.models import Exercise, Sets, Workouts
# Register your models here.
admin.site.register(Exercise)
admin.site.register(Sets)
admin.site.register(Workouts)
