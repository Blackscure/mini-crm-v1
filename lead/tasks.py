from celery import shared_task
from django.utils.timezone import now
from django.core.mail import send_mail

from reminders.models import Reminder

@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id, is_sent=False)
        # Simulate sending an email
        send_mail(
            subject="Reminder Notification",
            message=reminder.message,
            from_email="wekesabuyahi.com",
            recipient_list=["wekesabuyahi.com"], 
        )
        # Mark as sent
        reminder.is_sent = True
        reminder.save()
    except Reminder.DoesNotExist:
        print(f"Reminder with ID {reminder_id} does not exist or is already sent.")
