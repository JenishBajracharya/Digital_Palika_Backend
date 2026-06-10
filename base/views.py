from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import MainCategory
from .serializers import (
    CategorySerializer,
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
