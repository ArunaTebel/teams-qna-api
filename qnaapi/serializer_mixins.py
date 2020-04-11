from rest_framework import serializers


class ArchTeamsQnAModelPermissionsSerializerMixin(serializers.ModelSerializer):
    can_read = serializers.SerializerMethodField('_can_read')
    can_create = serializers.SerializerMethodField('_can_create')
    can_update = serializers.SerializerMethodField('_can_update')
    can_delete = serializers.SerializerMethodField('_can_delete')

    def _is_authenticated(self, obj):
        return ('request' in self.context) & hasattr(self.context['request'], 'user')

    def _get_current_user(self, obj):
        if ('request' in self.context) & hasattr(self.context['request'], 'user'):
            return self.context['request'].user

    def _get_current_arch_user(self, obj):
        if ('request' in self.context) & hasattr(self.context['request'], 'user'):
            return self.context['request'].user.archteamsqnauser

    def _is_current_arch_user_obj_owner(self, obj, owner_getter='owner'):
        return (self._is_authenticated(obj)) & (getattr(obj, owner_getter).id == self._get_current_arch_user(obj).id)

    def _can_read(self, obj):
        if obj is None:
            return True
        return self._is_authenticated(obj)

    def _can_create(self, obj):
        if obj is None:
            return True
        return self._is_authenticated(obj)

    def _can_update(self, obj):
        if obj is None:
            return True
        return self._is_current_arch_user_obj_owner(obj)

    def _can_delete(self, obj):
        if obj is None:
            return True
        return self._is_current_arch_user_obj_owner(obj)

    class Meta:
        abstract = True
