from celery import shared_task
from django.utils.timezone import now
from django.core.mail import send_mail
from reminders.models import Reminder

@shared_task
def send_reminder(reminder_id):
    try:
        
        reminder = Reminder.objects.get(id=reminder_id, is_sent=False)
        
        recipient_email = reminder.lead.email 

        print(f"Sending reminder: {reminder.message} to {recipient_email}")
        
    
        send_mail(
            subject="Reminder Notification",
            message=reminder.message,
            from_email="wekesabuyahi@gmail.com",  
            recipient_list=[recipient_email],
        )
        
       
        reminder.is_sent = True
        reminder.save()
    except Reminder.DoesNotExist:
        print(f"Reminder with ID {reminder_id} does not exist or is already sent.")
    except Exception as e:
        print(f"An error occurred while sending the reminder: {e}")
