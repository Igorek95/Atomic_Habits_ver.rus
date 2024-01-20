from datetime import datetime
from celery import shared_task
from django.apps import apps
from django.conf import settings
from django.utils.timezone import make_aware
from .telegram_utils import send_notification

@shared_task
def send_scheduled_notifications():
    """
    Отправляет уведомления по расписанию.

    Returns:
        None
    """
    Habit = apps.get_model('habits', 'Habit')
    current_time = datetime.now().time()

    habits_to_notify = Habit.objects.all()

    for habit in habits_to_notify:
        habit_time = datetime.strptime(habit.time, '%H:%M').time()

        if current_time >= habit_time:
            send_notification.delay(habit.user.telegram_chat_id, f"Время выполнить привычку: {habit.action} в {habit.place}")
