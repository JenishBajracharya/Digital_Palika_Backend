from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

# Models
from .models import (
    MainCategory,
    Darta,
    Pariyojana,
    RayakNo,
    MahilaIdentityCard,
    BalbalikaIdentityCard,
    ApangaIdentityCard,
    JanmaDarta,
    mrituDarta,
    biwahaDarta,
    migration_suchana,
    fileBhitra,
    file_prakar,
    rayak_khand_no,
    file_record,
    file_chalani,
    Chalani,
    KothaNumber,
    AarthikBarsa,
)

# Serializers
from .serializers import (
    CategorySerializer,
    DartaSerializer,
    PariyojanaSerializer,
    RayakNoSerializer,
    RegisterSerializer,
    LoginSerializer,
    identity_card_schema,

    MahilaIdentityCardSerializer,
    BalbalikaIdentityCardSerializer,
    ApangaIdentityCardSerializer,

    JanmaDartaSerializer,
    mrituDartaSerializer,
    biwahaDartaSerializer,
    migration_suchanaSerializer,

    fileBhitraSerializer,
    file_prakarSerializer,
    rayak_khand_no_Serializer,
    file_recordSerializer,
    file_chalaniSerializer,

    ChalaniSerializer,
    KothaNumberSerializer,
    AarthikBarsaSerializer,
)

User = get_user_model()


# =====================================================
# Authentication
# =====================================================

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


# =====================================================
# Category APIs
# =====================================================

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["get"])
    def form(self, request, pk=None):
        category = self.get_object()

        return Response({
            "category": {
                "id": category.id,
                "name": category.name
            },
            "identity_card_schemas": identity_card_schema()
        })


def category_list(request):
    categories = MainCategory.objects.all()

    return JsonResponse({
        "categories": [
            CategorySerializer(category).data
            for category in categories
        ]
    })


def category_form(request, category_id):
    category = get_object_or_404(MainCategory, pk=category_id)

    return JsonResponse({
        "category": {
            "id": category.id,
            "name": category.name,
        },
        "identity_card_schemas": identity_card_schema(),
    })


# =====================================================
# Darta APIs
# =====================================================

class DartaListCreateView(generics.ListCreateAPIView):
    queryset = Darta.objects.all()
    serializer_class = DartaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class DartaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Darta.objects.all()
    serializer_class = DartaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class DartaViewSet(ModelViewSet):
    queryset = Darta.objects.all()
    serializer_class = DartaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


# =====================================================
# Pariyojana APIs
# =====================================================

class PariyojanaListCreateView(generics.ListCreateAPIView):
    queryset = Pariyojana.objects.all()
    serializer_class = PariyojanaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class PariyojanaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pariyojana.objects.all()
    serializer_class = PariyojanaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class PariyojanaViewSet(ModelViewSet):
    queryset = Pariyojana.objects.all()
    serializer_class = PariyojanaSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


# =====================================================
# Rayak No APIs
# =====================================================

class RayakNoListCreateView(generics.ListCreateAPIView):
    queryset = RayakNo.objects.all()
    serializer_class = RayakNoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class RayakNoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RayakNo.objects.all()
    serializer_class = RayakNoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class RayakNoViewSet(ModelViewSet):
    queryset = RayakNo.objects.all()
    serializer_class = RayakNoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


# =====================================================
# Identity Card APIs
# =====================================================

class MahilaIdentityCardViewSet(ModelViewSet):
    queryset = MahilaIdentityCard.objects.all()
    serializer_class = MahilaIdentityCardSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class BalbalikaIdentityCardViewSet(ModelViewSet):
    queryset = BalbalikaIdentityCard.objects.all()
    serializer_class = BalbalikaIdentityCardSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class ApangaIdentityCardViewSet(ModelViewSet):
    queryset = ApangaIdentityCard.objects.all()
    serializer_class = ApangaIdentityCardSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


# =====================================================
# Registration Related APIs
# =====================================================

class JanmaDartaViewSet(ModelViewSet):
    queryset = JanmaDarta.objects.all()
    serializer_class = JanmaDartaSerializer


class MrituDartaViewSet(ModelViewSet):
    queryset = mrituDarta.objects.all()
    serializer_class = mrituDartaSerializer


class BiwahaDartaViewSet(ModelViewSet):
    queryset = biwahaDarta.objects.all()
    serializer_class = biwahaDartaSerializer


class MigrationSuchanaViewSet(ModelViewSet):
    queryset = migration_suchana.objects.all()
    serializer_class = migration_suchanaSerializer


# =====================================================
# File Management APIs
# =====================================================

class FileBhitraViewSet(ModelViewSet):
    queryset = fileBhitra.objects.all()
    serializer_class = fileBhitraSerializer


class FilePrakarViewSet(ModelViewSet):
    queryset = file_prakar.objects.all()
    serializer_class = file_prakarSerializer


class RayakKhandNoViewSet(ModelViewSet):
    queryset = rayak_khand_no.objects.all()
    serializer_class = rayak_khand_no_Serializer


class FileRecordViewSet(ModelViewSet):
    queryset = file_record.objects.all()
    serializer_class = file_recordSerializer


class FileChalaniViewSet(ModelViewSet):
    queryset = file_chalani.objects.all()
    serializer_class = file_chalaniSerializer


# =====================================================
# Chalani APIs
# =====================================================

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


# =====================================================
# Kotha Number APIs
# =====================================================

class KothaNumberViewSet(viewsets.ModelViewSet):
    queryset = KothaNumber.objects.all()
    serializer_class = KothaNumberSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["kotha_date"]

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


# =====================================================
# Aarthik Barsa APIs
# =====================================================

class AarthikBarsaViewSet(viewsets.ModelViewSet):
    queryset = AarthikBarsa.objects.all()
    serializer_class = AarthikBarsaSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["aarthik_barsa"]

    search_fields = [
        "aarthik_barsa",
        "description",
    ]

    ordering_fields = [
        "aarthik_barsa",
        "created_at",
    ]

    ordering = ["-aarthik_barsa"]
