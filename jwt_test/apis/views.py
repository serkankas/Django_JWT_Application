from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.utils.datastructures import MultiValueDictKeyError

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
def test_api_with_perm(request):
	user = request.user
	if (user.is_staff or user.groups.filter(name="editor").exists()):
		return Response({"message": f"The {user} able to perform this task."}, status=status.HTTP_200_OK)
	else:
		return Response({"message": f"The {user} cannot perform this tasks."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_with_api(request):
	user = request.user
	if (user.is_staff or user.groups.filter(name="editor").exists()):
		data = request.data
		try:
			username = data['username']
			query = User.objects.all().filter(username=username)
			if len(query) == 1:
				return Response({"message": f"The provided username \"{username}\" is already created."}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				password = data['password']
				password2 = data['password2']
				if password2 == password:
					new_user = User.objects.create_user(username=username, password=password)
					new_user.groups.add(Group.objects.get(name='standard'))
					return Response({"message": f"The {user} able to create {new_user} profile."}, status=status.HTTP_200_OK)
				else:
					return Response({"message": f"The provided credentials by {user} are not matching."}, status=status.HTTP_400_BAD_REQUEST)
		except MultiValueDictKeyError:
			return Response({"message": f"The provided credentials by {user} are not matching."}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({"message": f"The {user} cannot perform this tasks."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_with_api(request):
	user = request.user
	if (user.is_staff):
		data = request.data
		try:
			username = data['username']
			query = User.objects.all().filter(username=username)
			if len(query) == 0:
				return Response({"message": f"The provided username \"{username}\" is not avaliable."}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				delete_user = User.objects.get(username=username)
				delete_user.delete()
				return Response({"message": f"The {user} able to delete {delete_user} profile."}, status=status.HTTP_200_OK)
		except MultiValueDictKeyError:
			return Response({"message": f"The provided credentials by {user} are not matching."}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({"message": f"The {user} cannot perform this tasks."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_user_group_with_api(request):
	user = request.user
	if (user.is_staff or user.groups.filter(name="editor").exists()):
		data = request.data
		try:
			username = data['username']
			group_id = int(data['group_id'])
			query = User.objects.all().filter(username=username)
			if len(query) == 0:
				return Response({"message": f"The provided username \"{username}\" is not avaliable."}, status=status.HTTP_406_NOT_ACCEPTABLE)
			else:
				change_user = User.objects.get(username=username)
				if group_id == 1:
					change_user.groups.add(Group.objects.get(pk=1))
					change_user.groups.remove(Group.objects.get(pk=2))
				elif group_id == 2:
					change_user.groups.add(Group.objects.get(pk=2))
					change_user.groups.remove(Group.objects.get(pk=1))
				else:
					return Response({"message": f"The provided group id\"{group_id}\" is not avaliable."}, status=status.HTTP_406_NOT_ACCEPTABLE)
				return Response({"message": f"The {user} able to change {change_user}'s group."}, status=status.HTTP_200_OK)
		except [MultiValueDictKeyError, ValueError]:
			return Response({"message": f"The provided credentials by {user} are not matching."}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({"message": f"The {user} cannot perform this tasks."}, status=status.HTTP_401_UNAUTHORIZED)
