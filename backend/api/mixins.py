from rest_framework import mixins, viewsets


class CreateUpdateDestroyMixin(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(), )
        return super().get_permissions()