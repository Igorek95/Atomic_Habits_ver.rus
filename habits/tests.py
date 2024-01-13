import asyncio

from django.core.exceptions import ValidationError
from django.test import TestCase

from habits.telegram_utils import send_notification
from users.models import User
from .models import Habit, Action


class YourTestClassName(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@example.com', password='testpassword')

    def test_habit_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Home',
            time='Morning',
            action='Exercise',
            is_rewarded=True,
            is_pleasurable=True,
            is_public=True,
            frequency_days=7
        )
        self.assertEqual(habit.user, self.user)
        self.assertEqual(str(habit), 'Exercise')

    def test_habit_validation(self):
        related_habit = Habit.objects.create(
            user=self.user,
            place='Home',
            time='Evening',
            action='Meditate',
            is_pleasurable=True
        )
        habit = Habit(
            user=self.user,
            place='Gym',
            time='Afternoon',
            action='Read',
            is_pleasurable=True,
            related_habit=related_habit
        )
        with self.assertRaises(ValidationError) as context:
            habit.clean()

        self.assertIn('Приятные привычки не могут иметь связанную привычку.', str(context.exception))

    def test_action_creation(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Office',
            time='Noon',
            action='Lunch Break',
            is_public=True,
            frequency_days=1
        )
        action = Action.objects.create(
            user=self.user,
            habit=habit
        )
        self.assertEqual(action.user, self.user)
        self.assertEqual(action.habit, habit)
        self.assertIsNotNone(action.timestamp)


class TelegramNotificationTest(TestCase):
    def setUp(self):
        self.chat_id = '1391984681'
        self.notification_text = 'Тестовое уведомление из теста Django.'

    async def send_notification(self):
        await send_notification(self.chat_id, self.notification_text)

    def test_send_notification(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.send_notification())
