# Probably not the best library out there, but in the interest of time it's
# good enough
import pyshorteners

from rest_framework import viewsets
from apps.notes.models import Note
from apps.notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.is_valid()

        long_url = serializer.validated_data["content"]
        short_url = pyshorteners.Shortener().tinyurl.short(long_url)
        serializer.validated_data["short_url"] = short_url

        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
