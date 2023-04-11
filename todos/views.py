from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.pagination import CustomPageNumberPagination
from todos.serializers import TodoSerializer
from rest_framework import permissions, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from todos.models import Todo

class TodosAPIView(ListCreateAPIView):

    """
        Create & Get todos 
    """
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'description', 'is_complete']

    search_fields = ['id', 'title', 'description', 'is_complete']

    ordering_fields = ['id', 'title', 'description', 'is_complete']

    def perform_create(self, serializer):

        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):

    """
        Manage details for a todo : getById, update, delete
    """
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)

"""class CreateTodoAPIView(CreateAPIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):

        return serializer.save(owner=self.request.user)

class TodoListAPIView(ListAPIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    #queryset = Todo.objects.all() --> we want to overwrite this; so overwrite get_queryset(self)

    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
"""