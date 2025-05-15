from django.urls import path
from .views import ReminderCreate

urlpatterns = [
    path('reminder/', ReminderCreate.as_view()),
]
