from django.db import models
from rest_framework import serializers


from .models import (
    ApangaIdentityCard,
    BalbalikaIdentityCard,
    Darta,
    MainCategory,
    MahilaIdentityCard,

    Pariyojana,
    RayakNo,

    JanmaDarta,
    file_record,
    mrituDarta,
    biwahaDarta,
    migration_suchana,
    fileBhitra,
    file_prakar,
    rayak_khand_no,
    file_record,
    file_chalani,
    
    

)

from .models import *

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(source="phone_number", required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number')
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        request = self.context.get("request")

        user = authenticate(request=request, username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password.")

        if not user.is_active:
            raise serializers.ValidationError("This user account is disabled.")

        refresh = RefreshToken.for_user(user)

        return {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": getattr(user, "phone_number", None),
                "role": getattr(user, "role", None),
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ["id", "name"]


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



class DartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Darta
        fields = "__all__"


class PariyojanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pariyojana
        fields = "__all__"


class RayakNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RayakNo
        fields = "__all__"


class MahilaIdentityCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahilaIdentityCard
        fields = "__all__"


class BalbalikaIdentityCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalbalikaIdentityCard
        fields = "__all__"


class ApangaIdentityCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApangaIdentityCard
        fields = "__all__"



class JanmaDartaSerializer(serializers.ModelSerializer):
   class Meta:
       model = JanmaDarta
       fields = "__all__"



class mrituDartaSerializer(serializers.ModelSerializer):
   class Meta:
       model = mrituDarta
       fields = "__all__"

class biwahaDartaSerializer(serializers.ModelSerializer):
   class Meta:
       model = biwahaDarta
       fields = "__all__"

class migration_suchanaSerializer(serializers.ModelSerializer):
   class Meta:
       model = migration_suchana
       fields = "__all__"

class fileBhitraSerializer(serializers.ModelSerializer):
   class Meta:
       model = fileBhitra
       fields = "__all__"

class file_prakarSerializer(serializers.ModelSerializer):
   class Meta:
       model = file_prakar
       fields = "__all__"

class rayak_khand_no_Serializer(serializers.ModelSerializer):
   class Meta:
       model = rayak_khand_no
       fields = "__all__"

class file_recordSerializer(serializers.ModelSerializer):
   class Meta:
       model = file_record
       fields = "__all__"

class file_chalaniSerializer(serializers.ModelSerializer):
   class Meta:
       model = file_chalani
       fields = "__all__"

class ChalaniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chalani
        fields = "__all__"

class KothaNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = KothaNumber
        fields = "__all__"

class AarthikBarsaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AarthikBarsa
        fields = "__all__"

