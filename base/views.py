from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import MainCategory, Darta, Pariyojana, RayakNo

from .models import MainCategory, JanmaDarta, mrituDarta,biwahaDarta, migration_suchana, fileBhitra, file_prakar, rayak_khand_no, file_record, file_chalani


from .serializers import (
    CategorySerializer,
    DartaSerializer,
    PariyojanaSerializer,
    RayakNoSerializer,
    identity_card_schema,
    JanmaDartaSerializer,
    migration_suchanaSerializer,
    mrituDartaSerializer,
    biwahaDartaSerializer,
    migration_suchanaSerializer,
    fileBhitraSerializer,
    file_prakarSerializer,
    rayak_khand_no_Serializer,
    file_record,
    file_recordSerializer,
    file_chalaniSerializer,
)

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from rest_framework import generics
from .models import User
from .serializers import UserSerializer, RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = CategorySerializer
    @action(detail=True, methods=["get"])
    def form(self, request, pk=None):
        category = self.get_object()

        schema = identity_card_schema()

        return Response({
            "category": {
                "id": category.id,
                "name": category.name
            },
            "identity_card_schemas": schema
        })


def category_list(request):
    categories = MainCategory.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)



def category_form(request, category_id):
    category = get_object_or_404(MainCategory, pk=category_id)
    schema = identity_card_schema()
    return JsonResponse(
        {
            "category": {"id": category.id, "name": category.name},
            "identity_card_schemas": schema,
        }
    )



class DartaListCreateView(generics.ListCreateAPIView):
    queryset = Darta.objects.all()
    serializer_class = DartaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class DartaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Darta.objects.all()
    serializer_class = DartaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class PariyojanaListCreateView(generics.ListCreateAPIView):
    queryset = Pariyojana.objects.all()
    serializer_class = PariyojanaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class PariyojanaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pariyojana.objects.all()
    serializer_class = PariyojanaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class RayakNoListCreateView(generics.ListCreateAPIView):
    queryset = RayakNo.objects.all()
    serializer_class = RayakNoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class RayakNoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RayakNo.objects.all()
    serializer_class = RayakNoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]



class janma_darta_form(ModelViewSet):
    queryset = JanmaDarta.objects.all()
    serializer_class = JanmaDartaSerializer


class mrituDartaViewSet(ModelViewSet):
    queryset = mrituDarta.objects.all()
    serializer_class = mrituDartaSerializer

class biwahaDartaViewSet(ModelViewSet):
    queryset = biwahaDarta.objects.all()
    serializer_class = biwahaDartaSerializer

class migration_suchanaViewSet(ModelViewSet):
    queryset = migration_suchana.objects.all()
    serializer_class = migration_suchanaSerializer

class fileBhitraViewSet(ModelViewSet):
    queryset = fileBhitra.objects.all()
    serializer_class = fileBhitraSerializer

class file_prakarViewSet(ModelViewSet):
    queryset = file_prakar.objects.all()
    serializer_class = file_prakarSerializer

class rayak_khand_no_ViewSet(ModelViewSet):
    queryset = rayak_khand_no.objects.all()
    serializer_class = rayak_khand_no_Serializer

class file_recordViewSet(ModelViewSet):
    queryset = file_record.objects.all()
    serializer_class = file_recordSerializer

class file_chalaniViewSet(ModelViewSet):
    queryset = file_chalani.objects.all()
    serializer_class = file_chalaniSerializer

class ChalaniViewSet(viewsets.ModelViewSet):

    queryset = Chalani.objects.all()
    serializer_class = ChalaniSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "chalani_date",
        "letter_type",
        "receiving_branch",
    ]

    search_fields = [
        "chalani_no",
        "subject",
        "receiver_name",
        "receiver_address",
        "letter_type",
        "receiving_branch",
    ]

    ordering_fields = [
        "chalani_no",
        "created_at",
    ]

    ordering = ["-chalani_no"]
    
class KothaNumberViewSet(viewsets.ModelViewSet):

    queryset = KothaNumber.objects.all()
    serializer_class = KothaNumberSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "kotha_date",
    ]

    search_fields = [
        "kotha_no",
        "kotha_date",
        "description",
    ]

    ordering_fields = [
        "kotha_no",
        "created_at",
    ]

    ordering = ["-kotha_no"]
    
class AarthikBarsaViewSet(viewsets.ModelViewSet):

    queryset = AarthikBarsa.objects.all()
    serializer_class = AarthikBarsaSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "aarthik_barsa",
    ]

    search_fields = [
        "aarthik_barsa",
        "description",
    ]

    ordering_fields = [
        "aarthik_barsa",
        "created_at",
    ]

    ordering = ["-aarthik_barsa"]


