from datetime import datetime
from django.utils.timezone import make_aware, now 
from crm_mini_v1 import settings
from lead.tasks import send_reminder
from reminders.models import Reminder
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ReminderView(APIView):
    def post(self, request, *args, **kwargs):
        lead_id = request.data.get("lead_id")
        message = request.data.get("message")
        scheduled_time_str = request.data.get("scheduled_time")

        if not (lead_id and message and scheduled_time_str):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            scheduled_time = datetime.strptime(scheduled_time_str, "%Y-%m-%dT%H:%M:%SZ")
            if settings.USE_TZ:
                scheduled_time = make_aware(scheduled_time)
            reminder = Reminder.objects.create(
                lead_id=lead_id,
                message=message,
                scheduled_time=scheduled_time,
            )
            delay_time = (reminder.scheduled_time - now()).total_seconds() 
            send_reminder.apply_async(args=[reminder.id], countdown=max(0, delay_time))

            return Response({"success": "Reminder scheduled successfully!"}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response({"error": "Invalid datetime format. Use ISO 8601."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
