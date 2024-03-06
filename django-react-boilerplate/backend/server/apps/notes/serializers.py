from rest_framework import serializers
from apps.notes.models import Note
from django.core.validators import URLValidator


class NoteSerializer(serializers.ModelSerializer):

    def validate_content(self, data):
        validate_url = URLValidator()
        validate_url(data)
        return data

    class Meta:
        model = Note
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = ("id", "created_at", "created_by", "content", "short_url")
