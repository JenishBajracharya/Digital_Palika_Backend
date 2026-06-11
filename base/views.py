from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action


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

