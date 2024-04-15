from rest_framework import viewsets
from gym.models import Exercise, Sets, Workouts
from gym.serializers import ExerciseSerializer, SetsSerializer, WorkoutSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class SetsViewSet(viewsets.ModelViewSet):
    serializer_class = SetsSerializer
    queryset = Sets.objects.all()


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workouts.objects.all()
