from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from user_api.models import User
from user_api.serializers import UserSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_exist(request, email):
    if User.objects.filter(email=email).exists():
        return Response({'detail': 'true'}, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_418_IM_A_TEAPOT)
    return Response({'detail': 'false'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def users_get_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)