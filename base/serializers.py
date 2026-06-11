from django.db import models
from rest_framework import serializers

from .models import (
    ApangaIdentityCard,
    BalbalikaIdentityCard,
    MainCategory,
    MahilaIdentityCard,
    
)


def CategorySerializer(category: MainCategory) -> dict:
    return {
        "id": category.id,
        "name": category.name,
    }


def _serialize_field(field: models.Field) -> dict:
    field_data = {
        "name": field.name,
        "type": field.get_internal_type(),
        "required": not getattr(field, "blank", False),
        "editable": getattr(field, "editable", True),
    }

    max_length = getattr(field, "max_length", None)
    if max_length is not None:
        field_data["max_length"] = max_length

    if hasattr(field, "choices") and field.choices:
        field_data["choices"] = [choice for choice, _ in field.choices]

    if isinstance(field, (models.ForeignKey,)):
        field_data["related_model"] = f"{field.related_model._meta.app_label}.{field.related_model._meta.model_name}"

    return field_data


def model_schema(model_class: type[models.Model]) -> dict:
    return {
        "model": model_class.__name__,
        "fields": [
            _serialize_field(field)
            for field in model_class._meta.fields
            if not getattr(field, "auto_created", False) and not field.primary_key
        ],
    }


def identity_card_schema() -> list[dict]:
    return [
        model_schema(MahilaIdentityCard),
        model_schema(BalbalikaIdentityCard),
        model_schema(ApangaIdentityCard),
    ]


