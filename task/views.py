from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Add a Task (and List)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Return only pending tasks (is_completed=False) for GET requests
        return Task.objects.filter(is_completed=False)

# Mark Task as Completed (and retrieve task details)
class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
