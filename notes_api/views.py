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
        notes = Note.objects.filter(author_id=request.user.id, is_published=True)
        print(notes)
        if notes.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        print()
        _id = request.data.get('id', None)
        notes = Note.objects.filter(id=_id)
        if notes.count() == 0:
            note = NoteSerializer(data=request.data)
            if note.is_valid():
                note.save(author=request.user)
                return Response(note.data, status=status.HTTP_201_CREATED)
        else:
            note = NoteSerializer(data=request.data, instance=notes.first())
            if note.is_valid():
                note.save(author=request.user)
                return Response(note.data, status=status.HTTP_202_ACCEPTED)

        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes((permissions.IsAuthenticated,))
def note(request):
    pass


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_all_all(request):
    print(request.user)
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
