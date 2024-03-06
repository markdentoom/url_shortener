# Probably not the best library out there, but in the interest of time it's
# good enough
import pyshorteners

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.notes.models import Note
from apps.notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.is_valid()

        long_url = serializer.validated_data["content"]

        existing_url = Note.objects.filter(content=long_url).first()
        if existing_url:
            existing_url.request_count += 1
            existing_url.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        short_url = pyshorteners.Shortener().tinyurl.short(long_url)
        serializer.validated_data["short_url"] = short_url

        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
