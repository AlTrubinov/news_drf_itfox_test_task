from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import add_like, remove_like


class LikedMixin:
    @action(methods=["GET"], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        obj = self.get_object()
        add_like(obj, request.user)
        return Response()

    @action(methods=["GET"], detail=True, permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        remove_like(obj, request.user)
        return Response()
