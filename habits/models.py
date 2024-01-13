from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Habit(models.Model):
    """
    Модель для представления привычек.

    Модель хранит информацию о пользователях, их привычках, и связанных действиях.

    Attributes:
        user: Пользователь, создавший привычку.
        place: Место, в котором необходимо выполнять привычку.
        time: Время, когда необходимо выполнять привычку.
        action: Действие, представляющее привычку.
        is_rewarded: Признак вознаграждения после выполнения привычки.
        is_pleasurable: Признак приятной привычки.
        related_habit: Связанная привычка, к которой привязана текущая.
        is_public: Признак публичности привычки.
        frequency_days: Периодичность выполнения привычки в днях.

    Methods:
        __str__(): Возвращает строковое представление привычки.
        clean(): Проверяет валидность полей модели.

    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    action = models.CharField(max_length=255)
    is_rewarded = models.BooleanField(default=False)
    is_pleasurable = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    frequency_days = models.IntegerField(default=1)  # минимум 1 раз в 7 дней

    def __str__(self):
        """
        Возвращает строковое представление привычки.

        Returns:
            str: Строковое представление привычки.

        """
        return self.action

    def clean(self):
        """
        Проверяет валидность полей модели.

        Raises:
            ValidationError: В случае нарушения валидации.

        """
        if self.time_execution_seconds > 120:
            raise ValidationError(_('Время выполнения привычки не должно превышать 120 секунд.'))

        if self.is_pleasurable and (self.is_rewarded or self.related_habit):
            raise ValidationError(_('Приятная привычка не может иметь вознаграждения или связанной привычки.'))


        if self.frequency_days < 7:
            raise ValidationError(_('Привычку нельзя выполнять реже, чем 1 раз в 7 дней.'))

        super().clean()


class Action(models.Model):
    """
    Модель для представления действий, связанных с привычками.

    Модель хранит информацию о пользователях, привычках, и времени выполнения действия.

    Attributes:
        user: Пользователь, создавший действие.
        habit: Привычка, с которой связано действие.
        timestamp: Время создания действия.

    Methods:
        clean(): Проверяет валидность полей модели.

    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='actions')
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """
        Проверяет валидность полей модели.

        Raises:
            ValidationError: В случае нарушения валидации.

        """
        if self.user != self.habit.user:
            raise ValidationError(_('Привычка в действии должна принадлежать текущему пользователю.'))

        super().clean()
