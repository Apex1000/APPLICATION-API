from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    if user == group_name:
        return user
    else:
        return None

def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsSecretaryUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['SECRETARY']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

class IsSupervisorUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['SUPERVISOR']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['ADMIN']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

class IsUserSupervisorOrSecretary(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['SUPERVISOR','SECRETARY']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

class IsUserAdminOrSupervisorOrSecretary(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['ADMIN','SUPERVISOR','SECRETARY']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

class IsUserAdminOrSupervisorOrSecretaryOrWorker(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['ADMIN','SUPERVISOR','SECRETARY','WORKER']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission


class IsWorkerUser(permissions.BasePermission):
    required_groups = ['WORKER']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user.userrole.name, self.required_groups)
        return request.user and has_group_permission