from django.core.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet


class ModelWithOwnerLoggedInCreateMixin(ModelViewSet):
    def restrict_if_obj_not_permitted(self, permission_type='can_update'):
        serializer = self.get_serializer(self.get_object())
        if not serializer.data[permission_type]:
            raise PermissionDenied()
