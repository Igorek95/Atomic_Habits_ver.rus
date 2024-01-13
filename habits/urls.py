from django.urls import path

from .apps import HabitsConfig
from .views import (
    HabitListCreateView, HabitDetailView, PublicHabitListView, CreatePublicHabitView,
    ActionListCreateView, ActionRetrieveUpdateDestroyView
)

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListCreateView.as_view(), name='habit-list-create'),
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('public-habits/', PublicHabitListView.as_view(), name='public-habit-list'),
    path('create-public-habit/', CreatePublicHabitView.as_view(), name='create-public-habit'),

    path('actions/', ActionListCreateView.as_view(), name='action-list-create'),
    path('actions/<int:pk>/', ActionRetrieveUpdateDestroyView.as_view(), name='action-retrieve-update-destroy'),
]
