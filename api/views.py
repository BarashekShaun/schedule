import time
from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer, OrganizationSerializer, EventFilter


@permission_classes((IsAuthenticated,))
class EventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = EventFilter


@permission_classes((IsAuthenticated,))
class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@sync_to_async
def create_event(request):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        time.sleep(60)
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_organization(request):
    if request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
