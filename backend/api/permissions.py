from rest_framework.permissions import BasePermission

from tasks.models import Task


class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
