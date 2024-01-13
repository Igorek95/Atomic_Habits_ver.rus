from rest_framework import permissions


class HabitPermission(permissions.BasePermission):
    """
    Права доступа для объектов привычек.

    Разрешает доступ только для владельца привычки на основе методов запроса.

    - `GET`, `HEAD`, `OPTIONS`: Разрешено для всех пользователей.
    - `POST`, `PUT`, `PATCH`, `DELETE`: Разрешено только владельцу привычки.

    Attributes:
        request: Запрос к API.
        view: Представление, обрабатывающее запрос.
        obj: Экземпляр привычки, к которому осуществляется доступ.

    Methods:
        has_object_permission(request, view, obj): Проверяет права доступа к конкретному объекту.

    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет права доступа к конкретному объекту привычки.

        Args:
            request: Запрос к API.
            view: Представление, обрабатывающее запрос.
            obj: Экземпляр привычки, к которому осуществляется доступ.

        Returns:
            bool: Разрешено или запрещено.

        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
