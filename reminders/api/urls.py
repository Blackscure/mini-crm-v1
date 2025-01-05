from django.urls import path

from reminders.api.views import ReminderView


urlpatterns = [
    path('reminders/', ReminderView.as_view(), name='reminders'),
]
