from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView,CreateAPIView

from classes.models import Classroom
from .serializers import ClassListSerializer,ClassroomDetailsSerializer,CreatClassroomSerializer,UpdateClassroomSerializer


# Create your views here.
class APIListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer

class APIDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'teacher_id'

class APICreateView(CreateAPIView):
    serializer_class = CreatClassroomSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user,)

class APIUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = UpdateClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'teacher_id'

class APIDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'teacher_id'
