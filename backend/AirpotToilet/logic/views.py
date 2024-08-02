from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff,Day,Allocation,Feedback
from .serializers import StaffSerializer,DaySerializer,AllocationSerializer,FeedbackSerializer
# Create your views here.
# STAFF
@api_view(['POST'])
def createStaff(request):
    serializer = StaffSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getStaff(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def updateStaff(request, Sid):
    try:
        staff = Staff.objects.get(Sid = Sid)
        serializer = StaffSerializer(staff, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' staff {Sid} does not exist')

@api_view(['DELETE'])
def deleteStaff(request, Sid):
    try:
        staff = Staff.objects.get(Sid = Sid)
        staff.delete()
        return Response("Deleted Sucessifully", status=200)
    except:
        return Response(f' staff {Sid} does not exist')
    




#  FEEDBACK
@api_view(['POST'])
def createFeedback(request):
    serializer = FeedbackSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getFeedback(request):
    feedback = Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def updateFeedback(request, Fid):
    try:
        feedback = Feedback.objects.get(Fid = Fid)
        serializer = FeedbackSerializer(feedback, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response(f' staff {Fid} does not exist')

@api_view(['DELETE'])
def deleteFeedback(request, Fid):
    try:
        staff = Staff.objects.get(Fid = Fid)
        staff.delete()
        return Response("Deleted Sucessifully", status=200)
    except:
        return Response(f' Feedback {Fid} does not exist')
