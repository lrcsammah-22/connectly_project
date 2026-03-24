from rest_framework.permissions import BasePermission

class IsPostAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_author = obj.author == request.user
        is_admin = request.user.groups.filter(name='Admin').exists()
    
        return is_author or is_admin
    
class IsAdminUserCustom(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.groups.filter(name='admin').exists()
        )