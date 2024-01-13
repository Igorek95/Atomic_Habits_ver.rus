from rest_framework import serializers

from .models import Habit, Action


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для привычек.

    Attributes:
        Meta (class): Класс метаданных для сериализатора.
            model (Model): Модель, которую сериализует сериализатор.
            fields (str): Список полей, которые будут включены в сериализованный вывод.

    """
    class Meta:
        model = Habit
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для действий.

    Attributes:
        Meta (class): Класс метаданных для сериализатора.
            model (Model): Модель, которую сериализует сериализатор.
            fields (str): Список полей, которые будут включены в сериализованный вывод.

    """
    class Meta:
        model = Action
        fields = '__all__'
