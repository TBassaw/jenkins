from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsAuthorOrReadOnly

class TodoViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
