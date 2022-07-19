from .models import Subject, Sheet, Reference, Tutorial, Exam
from .serializers import ExamSerializer, ReferenceSerializer, SubjectSerializer, SheetSerializer, TutorialSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, status, generics
from rest_framework.filters import SearchFilter, OrderingFilter


@api_view(['GET'])
def end_points(request):
    endPoints = [
        {
            "endpoint": "subject_data/",
            "method": "GET",
            "description": "get all subjects list and retreive the whith extra action"
        },
        {
            "endpoint": "search_for_subject/",
            "method": "GET",
            "description": "search for subject by it name"
        },
    ]
    return Response(endPoints)


# get all subject data and all four component
class SubjectDataViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']

    # block hackers to add any data
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(methods=['get'], detail=True)
    def sheets(self, request, pk=None, *args, **kwargs):
        sheet = Sheet.objects.filter(subject=pk)
        serializer = SheetSerializer(sheet, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def references(self, request, pk=None, *args, **kwargs):
        reference = Reference.objects.filter(subject=pk)
        serializer = ReferenceSerializer(reference, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def tutorials(self, request, pk=None, *args, **kwargs):
        tutorial = Tutorial.objects.filter(subject=pk)
        serializer = TutorialSerializer(tutorial, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def exams(self, request, pk=None, *args, **kwargs):
        exam = Exam.objects.filter(subject=pk)
        serializer = ExamSerializer(exam, many=True)
        return Response(serializer.data)


# search fo a subject by put (?search='name of subject') after URL
class SearchForSubject(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
