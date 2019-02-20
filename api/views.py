from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	CreateAPIView,
	DestroyAPIView)
from classes.models import Classroom
from .serializers import (
	ClassroomListSerializer,
	ClassroomCreateUpdateSerializer,
	ClassroomDetailSerializer,
	)

class ListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class DetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class CreateView(CreateAPIView):
	serializer_class = ClassroomCreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)


class UpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class DeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
	
