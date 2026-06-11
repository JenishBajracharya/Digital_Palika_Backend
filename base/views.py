from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import MainCategory, Darta, Pariyojana, RayakNo
from .serializers import (
    CategorySerializer,
    DartaSerializer,
    PariyojanaSerializer,
    RayakNoSerializer,
    identity_card_schema,
)


def category_list(request):
    categories = MainCategory.objects.all()
    data = [CategorySerializer(category) for category in categories]
    return JsonResponse({"categories": data})


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


