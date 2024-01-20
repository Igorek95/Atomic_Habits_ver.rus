from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit, Action
from .pagination import CustomPageNumberPagination
from .permissions import HabitPermission
from .serializers import HabitSerializer, ActionSerializer
from .telegram_utils import send_notification


class HabitListCreateView(generics.ListCreateAPIView):
    """
    API-конечная точка для списка и создания привычек.

    - `GET`: Возвращает список привычек для аутентифицированного пользователя.
    - `POST`: Создает новую привычку для аутентифицированного пользователя.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, HabitPermission]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API-конечная точка для получения, обновления и удаления привычек.

    - `GET`: Возвращает детали определенной привычки.
    - `PUT`: Обновляет определенную привычку.
    - `DELETE`: Удаляет определенную привычку.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, HabitPermission]


class PublicHabitListView(generics.ListAPIView):
    """
    API-конечная точка для списка публичных привычек.

    - `GET`: Возвращает список публичных привычек.
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPageNumberPagination


class CreatePublicHabitView(generics.CreateAPIView):
    """
    API-конечная точка для создания публичной привычки.

    - `POST`: Создает новую публичную привычку для аутентифицированного пользователя.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, HabitPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_public=True)


class ActionListCreateView(generics.ListCreateAPIView):
    """
    API-конечная точка для списка и создания действий.

    - `GET`: Возвращает список действий для аутентифицированного пользователя.
    - `POST`: Создает новое действие для аутентифицированного пользователя.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API-конечная точка для получения, обновления и удаления действий.

    - `GET`: Возвращает детали определенного действия.
    - `PUT`: Обновляет определенное действие.
    - `DELETE`: Удаляет определенное действие.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]


@receiver(pre_delete, sender=Habit)
def habit_pre_delete(sender, instance, **kwargs):
    """
    Обработчик сигнала для события предварительного удаления объекта модели Habit.
    Отправляет уведомление о удалении привычки.

    Args:
        sender: Отправитель сигнала.
        instance: Экземпляр модели Habit, который будет удален.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        None
    """
    check_habit_deletion(instance)


from datetime import datetime
from django.template import Template, Context


def check_habit_time(habit):
    """
    Проверяет, наступило ли время выполнения привычки, и отправляет уведомление, если это так.

    Args:
        habit: Экземпляр привычки для проверки.

    Returns:
        None
    """
    current_time = datetime.now().time()
    habit_time = datetime.strptime(habit.time, '%H:%M').time()

    if current_time >= habit_time:
        template_text = "Я буду {{ action }} в {{ time }} в {{ place }}"
        template = Template(template_text)
        context = Context({'action': habit.action, 'time': habit.time, 'place': habit.place})
        formatted_text = template.render(context)

        send_notification(chat_id=habit.user.telegram_chat_id, text=formatted_text)


def check_habit_deletion(habit):
    """
    Отправляет уведомление о удалении привычки.

    Args:
        habit: Экземпляр привычки, который будет удален.

    Returns:
        None
    """
    send_notification(chat_id=habit.user.telegram_chat_id, text="Привычка удалена.")
