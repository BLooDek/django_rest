from django.shortcuts import render

# Create your views here.
# serializer = EventSerializer(events, context={'user': request.user}, many=True)
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from notes_api.models import Note
from notes_api.serializers import NoteSerializer


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes((permissions.IsAuthenticated,))
def get_all(request):
    print(request.user)
    if request.method == 'GET':
        notes = Note.objects.filter(author_id=request.user.id)
        print(notes)
        if notes.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        note = NoteSerializer(context={'request': request}, data=request.data)
        if note.is_valid():
            note.save()
            return Response(note.data, status=status.HTTP_201_CREATED)
        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes((permissions.IsAuthenticated,))
def note(request):
    pass
