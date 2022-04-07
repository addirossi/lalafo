from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    #работа с одним объектом (retrieve, update, destroy)
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user
