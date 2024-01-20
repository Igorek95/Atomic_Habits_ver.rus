from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RewardOrHabitValidator:
    def __init__(self, add_habit_field, reward_field, is_nice_field) -> None:
        self.add_habit_field = add_habit_field
        self.reward_field = reward_field
        self.is_nice_field = is_nice_field

    def __call__(self, value):
        if value.get(self.add_habit_field) and value.get(self.reward_field):
            raise serializers.ValidationError("Нельзя одновременно выбрать связанную привычку и награду.")
        elif not value.get(self.is_nice_field) and \
                (not value.get(self.add_habit_field) and not value.get(self.reward_field)):
            raise serializers.ValidationError("Укажите награду или приятную связанную привычку.")


class TimeToDoLess120Validator:
    def __init__(self, time_to_do_field) -> None:
        self.time_to_do_field = time_to_do_field

    def __call__(self, value):
        if value.get(self.time_to_do_field, 120) > 120:
            raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")


class AdditionalHabitIsNiceValidator:
    def __init__(self, habit_field) -> None:
        self.habit_field = habit_field

    def __call__(self, value):
        if value.get(self.habit_field):
            if not value.get(self.habit_field).is_nice:
                raise serializers.ValidationError("Связанная привычка должна быть приятной.")


class NiceHabitNoRewardValidator:
    def __init__(self, is_nice_field, add_habit_field, reward_field) -> None:
        self.is_nice_field = is_nice_field
        self.add_habit_field = add_habit_field
        self.reward_field = reward_field

    def __call__(self, value):
        if value.get(self.is_nice_field) and \
                (value.get(self.add_habit_field) or value.get(self.reward_field)):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки.")


class PeriodWeeklyOrLessValidator:
    def __init__(self, period_field) -> None:
        self.period_field = period_field

    def __call__(self, value):
        if value.get(self.period_field) > 7:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


class IsPublicHabitHasPublicAddHabitValidator:
    def __init__(self, is_public_fied, add_habit_field) -> None:
        self.is_public_fied = is_public_fied
        self.add_habit_field = add_habit_field

    def __call__(self, value):
        if value.get(self.is_public_fied) and value.get(self.add_habit_field):
            if not value.get(self.add_habit_field).is_public:
                raise serializers.ValidationError("Связанная привычка публичной привычки должна быть тоже публичной.")


class UserHasTelegramIDValidator:
    def __init__(self, user_field) -> None:
        self.user_field = user_field

    def __call__(self, value):
        if not value.get(self.user_field).telegram_id:
            raise serializers.ValidationError("Вы должны добавить Telegram ID в профиль для подписки.")
