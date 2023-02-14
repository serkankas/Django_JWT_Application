from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

#from . import permissions

# Create your views here.
@api_view(['GET'])
def test_api(request):
	return Response({"message":"API has been called Successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api_with_auth(request):
	return Response({"message":f"The user {request.user} has successfully called the API!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_user_with_api(request):
	user = request.user
	if (user.is_staff or user.groups.filter(name="editor").exists()):
		return Response({"message": f"The {user} able to perform this task."}, status=status.HTTP_200_OK)
	else:
		return Response({"message": f"The {user} cannot perform this tasks."}, status=status.HTTP_401_UNAUTHORIZED)