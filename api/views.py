from django.http import HttpResponse, JsonResponse

from .models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from rest_framework import generics, mixins
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class TaskAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = TaskSerializer
    def get_queryset(self):
        qs = Task.objects.all()
        query = self.request.GET.get("q")
        if(query) is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(description__icontains=query)
                    ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field        = 'pk'
    serializer_class    = TaskSerializer
    # permission_classes  = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Task.objects.all()


class SubTaskAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = SubtaskSerializer
    def get_queryset(self):
        qs = Subtask.objects.all()
        query = self.request.GET.get("q")
        if(query) is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(description__icontains=query)
                    ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
