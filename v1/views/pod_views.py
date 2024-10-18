from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from v1.utils import validate_tcg_type
from ..serializers.pod_serializer import PodSerializer
from ..models.pod_model import Pod


@api_view(['GET', 'POST'])
def pod_list(request):
    if request.method == 'GET':
        return get_pod_list()
    elif request.method == 'POST':
        return create_pod(request)

def get_pod_list():
    pods = Pod.objects.all()
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)

def create_pod(request: dict):
    # The code below might be saving the error we get back from the validation check as the tcg_type which is what we don't want. Make sure this isn't the case in the Views tests and Postman.
    tcg_type_validation_check = validate_tcg_type(request.data["tcg_type"])

    new_pod_data = {
        "name": request.data["name"],
        "tcg_type": tcg_type_validation_check
    }

    serializer = PodSerializer(new_pod_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pod_details(request, pod_id: int):
    try:
        pod = Pod.objects.get(pk=pod_id)
    except Pod.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_specific_pod(pod)
    elif request.method == 'PUT':
        return update_specific_pod(pod, request)
    elif request.method == 'DELETE':
        return delete_pod(pod)

def get_specific_pod(pod: Pod):
    serializer = PodSerializer(pod)
    return Response(serializer.data)

def update_specific_pod(pod: Pod, request):
    # ensure that the tcg_type validation check can happen here too.

    pod_data = PodSerializer(pod, data=request.data, partial=True)
    if pod_data.is_valid():
        pod_data.save()
        return Response(pod_data.data)
    return Response(pod_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_pod(pod: Pod):
    pod.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)