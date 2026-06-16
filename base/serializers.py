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
    karmachari,
    woda,
    pratinidhi,
    patraKoKisim,
    sakha_thapnuhos,
    sadasya_thapnuhos,
    

)

from .models import *



from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
        ]


from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "role",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
            phone=validated_data.get("phone"),
            role=validated_data.get("role", "citizen"),
        )
        return user
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"


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


from .models import Province, District, Municipality, Ward


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(
        source="province.name",
        read_only=True
    )

    class Meta:
        model = District
        fields = "__all__"


class MunicipalitySerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(
        source="district.name",
        read_only=True
    )

    class Meta:
        model = Municipality
        fields = "__all__"


class WardSerializer(serializers.ModelSerializer):
    municipality_name = serializers.CharField(
        source="municipality.name",
        read_only=True
    )

    class Meta:
        model = Ward
        fields = "__all__"


from .models import (
    Farmer, Land, Crop, CropProduction, Inventory, 
    Livestock, SoilReport, Sale, CropDisease, WeatherData, Recommendation
)

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class CropProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropProduction
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'


class SoilReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilReport
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    # Optional auto-calculation of total price if not provided by the client
    class Meta:
        model = Sale
        fields = '__all__'

    def validate(self, data):
        if not data.get('total_price'):
            data['total_price'] = data['quantity'] * data['price_per_kg']
        return data


class CropDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropDisease
        fields = '__all__'


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'



from .models import DeviceToken, NotificationLog, User

class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DeviceTokenSerializer(serializers.ModelSerializer):
    user_detail = UserMinimalSerializer(source='user', read_only=True)

    class Meta:
        model = DeviceToken
        fields = ['id', 'user', 'user_detail', 'fcm_token', 'device_type', 'is_active', 'updated_at']


class BroadcastNotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    body = serializers.CharField(required=True)
    image = serializers.ImageField(required=False, allow_null=True)


class TestNotificationSerializer(serializers.Serializer):
    fcm_token = serializers.CharField(required=True)
    title = serializers.CharField(max_length=255, required=True)
    body = serializers.CharField(required=True)

class karmachariSerializer(serializers.ModelSerializer):

    class Meta:
        model = karmachari
        fields = "__all__"

class wodaSerializer(serializers.ModelSerializer):

    class Meta:
        model = woda
        fields = "__all__"

class pratinidhiSerializer(serializers.ModelSerializer):

    class Meta:
        model = pratinidhi
        fields = "__all__"

class patraKoKisimSerializer(serializers.ModelSerializer):

    class Meta:
        model = patraKoKisim
        fields = "__all__"

class sakha_thapnuhosSerializer(serializers.ModelSerializer):

    class Meta:
        model = sakha_thapnuhos
        fields = "__all__"

class sadasya_thapnuhosSerializer(serializers.ModelSerializer):

    class Meta:
        model = sadasya_thapnuhos
        fields = "__all__"

