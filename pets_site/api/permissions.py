"""
Содержит кастомные пермишены:

- Доступ на уровне владельца;
- ...
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Кастомный пермишен, который даст доступ на уровне владельца"""

    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user
                or request.method in permissions.SAFE_METHODS)
