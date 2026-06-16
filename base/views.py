from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import MainCategory, Darta, Pariyojana, RayakNo

from .models import MainCategory, JanmaDarta, mrituDarta,biwahaDarta, migration_suchana, fileBhitra, file_prakar, rayak_khand_no, file_record, file_chalani, karmachari, woda, pratinidhi,patraKoKisim,sakha_thapnuhos, sadasya_thapnuhos


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
    karmachariSerializer,
    wodaSerializer,
    pratinidhiSerializer,
    patraKoKisimSerializer,
    sakha_thapnuhosSerializer,
    sadasya_thapnuhosSerializer,
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


janma_darta_form = JanmaDartaViewSet
mrituDartaViewSet = MrituDartaViewSet
biwahaDartaViewSet = BiwahaDartaViewSet
migration_suchanaViewSet = MigrationSuchanaViewSet
fileBhitraViewSet = FileBhitraViewSet
file_prakarViewSet = FilePrakarViewSet
rayak_khand_no_ViewSet = RayakKhandNoViewSet
file_recordViewSet = FileRecordViewSet
file_chalaniViewSet = FileChalaniViewSet

class ChalaniViewSet(viewsets.ModelViewSet):

    queryset = Chalani.objects.all()
    serializer_class = ChalaniSerializer


class karmachariViewSet(viewsets.ModelViewSet):
    queryset = karmachari.objects.all()
    serializer_class = karmachariSerializer

class wodaViewSet(viewsets.ModelViewSet):
    queryset = woda.objects.all()
    serializer_class = wodaSerializer

class pratinidhiViewSet(viewsets.ModelViewSet):
    queryset = pratinidhi.objects.all()
    serializer_class = pratinidhiSerializer

class patraKoKisimViewSet(viewsets.ModelViewSet):
    queryset = patraKoKisim.objects.all()   
    serializer_class = patraKoKisimSerializer


class sakha_thapnuhosViewSet(viewsets.ModelViewSet):
    queryset = sakha_thapnuhos.objects.all()
    serializer_class = sakha_thapnuhosSerializer

class sadasya_thapnuhosViewSet(viewsets.ModelViewSet):
    queryset = sadasya_thapnuhos.objects.all() 
    serializer_class = sadasya_thapnuhosSerializer    




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


from rest_framework import viewsets

from .models import (
    Province,
    District,
    Municipality,
    Ward,
)

from .serializers import (
    ProvinceSerializer,
    DistrictSerializer,
    MunicipalitySerializer,
    WardSerializer,
)


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.select_related("province")
    serializer_class = DistrictSerializer


class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.select_related(
        "district",
        "district__province"
    )
    serializer_class = MunicipalitySerializer


class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.select_related(
        "municipality",
        "municipality__district"
    )
    serializer_class = WardSerializer


def districts_by_province(request, province_id):
    districts = District.objects.filter(province_id=province_id)
    serializer = DistrictSerializer(districts, many=True)
    return JsonResponse(serializer.data, safe=False)


def municipalities_by_district(request, district_id):
    municipalities = Municipality.objects.filter(district_id=district_id)
    serializer = MunicipalitySerializer(municipalities, many=True)
    return JsonResponse(serializer.data, safe=False)


def wards_by_municipality(request, municipality_id):
    wards = Ward.objects.filter(municipality_id=municipality_id)
    serializer = WardSerializer(wards, many=True)
    return JsonResponse(serializer.data, safe=False)


from rest_framework import viewsets
from .models import (
    Farmer, Land, Crop, CropProduction, Inventory, 
    Livestock, SoilReport, Sale, CropDisease, WeatherData, Recommendation
)
from .serializers import (
    FarmerSerializer, LandSerializer, CropSerializer, CropProductionSerializer,
    InventorySerializer, LivestockSerializer, SoilReportSerializer, SaleSerializer,
    CropDiseaseSerializer, WeatherDataSerializer, RecommendationSerializer
)

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer


class CropProductionViewSet(viewsets.ModelViewSet):
    queryset = CropProduction.objects.all()
    serializer_class = CropProductionSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class LivestockViewSet(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer


class SoilReportViewSet(viewsets.ModelViewSet):
    queryset = SoilReport.objects.all()
    serializer_class = SoilReportSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CropDiseaseViewSet(viewsets.ModelViewSet):
    queryset = CropDisease.objects.all()
    serializer_class = CropDiseaseSerializer


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import DeviceToken, NotificationLog, User
from .serializers import (
    DeviceTokenSerializer, 
    BroadcastNotificationSerializer, 
    TestNotificationSerializer,
    UserMinimalSerializer
)
from .firebase_config import send_multicast_notification

# 1. UI Segment: Get Registered Devices List & Dropdowns
class DeviceTokenListView(generics.ListCreateAPIView):
    """
    Handles fetching registered devices and manually saving a token 
    (UI blocks: 'दर्ता भएका डिभाइसहरू' and 'FCM Token दर्ता गर्नुहोस्')
    """
    queryset = DeviceToken.objects.all().order_by('-updated_at')
    serializer_class = DeviceTokenSerializer


class UserDropdownListView(generics.ListAPIView):
    """Helper endpoint to populate user dropdown selection"""
    queryset = User.objects.all()
    serializer_class = UserMinimalSerializer


# 2. UI Segment: Broadcast Notification Form (सबैलाई नोटिफिकेशन पठाउनुहोस्)
class BroadcastNotificationView(APIView):
    def post(self, request):
        serializer = BroadcastNotificationSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            image_file = serializer.validated_data.get('image', None)
            
            # Save historical log
            log = NotificationLog.objects.create(
                title=title,
                body=body,
                image=image_file,
                target_type='broadcast',
                sender=request.user if request.user.is_authenticated else None
            )
            
            # Fetch all active target tokens
            active_devices = DeviceToken.objects.filter(is_active=True)
            tokens = [device.fcm_token for device in active_devices]
            
            if not tokens:
                return Response({"message": "No active device tokens found."}, status=status.HTTP_400_BAD_REQUEST)
            
            image_url = request.build_absolute_uri(log.image.url) if log.image else None
            
            # Process with Firebase
            invalid_tokens = send_multicast_notification(tokens, title, body, image_url)
            
            # Clean up corrupted/expired devices database entries asynchronously
            if invalid_tokens:
                DeviceToken.objects.filter(fcm_token__in=invalid_tokens).update(is_active=False)
                
            return Response({
                "message": f"Broadcast triggered successfully to {len(tokens)} devices.",
                "failed_tokens_cleaned": len(invalid_tokens)
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3. UI Segment: Single Device Testing Form (एउटा डिभाइसमा परीक्षण गर्नुहोस्)
class TestNotificationView(APIView):
    def post(self, request):
        serializer = TestNotificationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['fcm_token']
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            
            # Process single notification
            invalid_tokens = send_multicast_notification([token], title, body)
            
            if invalid_tokens:
                DeviceToken.objects.filter(fcm_token=token).update(is_active=False)
                return Response({"message": "Device token is expired/invalid. Disabling in DB."}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({"message": "Test notification sent successfully."}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
