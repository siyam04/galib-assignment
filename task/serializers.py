from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed', 'created_at']
        extra_kwargs = {
            'is_completed': {'default': False},  # Default to False if not provided
            'created_at': {'read_only': True}    # Automatically set, not editable
        }

    def validate_title(self, value):
        # Ensure title is at least 3 characters long and not just whitespace
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long and not just whitespace.")
        return value
