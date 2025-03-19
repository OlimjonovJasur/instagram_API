from datetime import timedelta, datetime

from django.utils.timezone import now
from rest_framework.permissions import BasePermission


class GetOrPostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsNotAliUpdateDelete(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.username == 'ali':
            return request.method not in ['PUT', 'PATCH', 'DELETE']
        return True



# bu 2 minutdan keyin o'chirishga ruxsat bermaydi
class NotDeleteAfterTwoMinutes(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author != request.user:
            return False

        if request.method == "DELETE" and (now() - obj.created_at) > timedelta(minutes=2):
            return False

        return True


class IsWeekday(BasePermission):
    def has_permission(self, request, view):
        today = datetime.today().weekday()
        return 0 <= today <= 4



