from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseInstanceListView(APIView):
    def get(self, request, year, semester):
        course_instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(course_instances, many=True)
        return Response(serializer.data)

    def post(self, request, year, semester):
        serializer = CourseInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseInstanceDetailView(APIView):
    def get(self, request, year, semester, pk):
        course_instance = CourseInstance.objects.get(pk=pk, year=year, semester=semester)
        serializer = CourseInstanceSerializer(course_instance)
        return Response(serializer.data)

    def delete(self, request, year, semester, pk):
        course_instance = CourseInstance.objects.get(pk=pk, year=year, semester=semester)
        course_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)