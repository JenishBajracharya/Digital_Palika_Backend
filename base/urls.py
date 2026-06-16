from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    FarmerViewSet, LandViewSet, CropViewSet, CropProductionViewSet,
    InventoryViewSet, LivestockViewSet, SoilReportViewSet, SaleViewSet,
    CropDiseaseViewSet, WeatherDataViewSet, RecommendationViewSet,DeviceTokenListView, 
    UserDropdownListView, 
    BroadcastNotificationView, 
    TestNotificationView
)



urlpatterns = [
 
    path("janma-darta/", views.JanmaDartaViewSet.as_view({"get": "list", "post": "create"})),
    path("janma-darta/<int:pk>/", views.JanmaDartaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
   
    path("mritu-darta/", views.MrituDartaViewSet.as_view({"get": "list", "post": "create"})),
    path("mritu-darta/<int:pk>/", views.mrituDartaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),  
    
    path("biwaha-darta/", views.BiwahaDartaViewSet.as_view({"get": "list", "post": "create"})),
    path("biwaha-darta/<int:pk>/", views.BiwahaDartaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),  
    
    path("migration-suchana/", views.MigrationSuchanaViewSet.as_view({"get": "list", "post": "create"})),
    path("migration-suchana/<int:pk>/", views.MigrationSuchanaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),  
    
    path("file-bhitra/", views.FileBhitraViewSet.as_view({"get": "list", "post": "create"})),
    path("file-bhitra/<int:pk>/", views.fileBhitraViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),  
    
    path("file-prakar/", views.FilePrakarViewSet.as_view({"get": "list", "post": "create"})),
    path("file-prakar/<int:pk>/", views.FilePrakarViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),   
    
    path("rayak_khand_no/", views.RayakKhandNoViewSet.as_view({"get": "list", "post": "create"})),
    path("rayak_khand_no/<int:pk>/", views.RayakKhandNoViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),   
    
    path("file-record/", views.FileRecordViewSet.as_view({"get": "list", "post": "create"})),
    path("file-record/<int:pk>/", views.file_recordViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),  
   
    path("file-chalani/", views.FileChalaniViewSet.as_view({"get": "list", "post": "create"})),
    path("file-chalani/<int:pk>/", views.FileChalaniViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    path( "provinces/", views.ProvinceViewSet.as_view({"get": "list", "post": "create"}),name="province-list"),
    path("provinces/<int:pk>/",views.ProvinceViewSet.as_view({"get": "retrieve",   "put": "update",   "patch": "partial_update",    "delete": "destroy"    }),    name="province-detail"),
    path(  "districts/",  views.DistrictViewSet.as_view({"get": "list", "post": "create"    }), name="district-list"),   
    path("districts/<int:pk>/",  views.DistrictViewSet.as_view({"get": "retrieve", "put": "update",   "patch": "partial_update",   "delete": "destroy"    }),    name="district-detail" ),
    path("municipalities/", views.MunicipalityViewSet.as_view({"get": "list","post": "create"}),name="municipality-list"),   
    path("municipalities/<int:pk>/",views.MunicipalityViewSet.as_view({"get": "retrieve","put": "update","patch": "partial_update","delete": "destroy"}),name="municipality-detail"),
    path("wards/",views.WardViewSet.as_view({"get": "list","post": "create"}),name="ward-list"),    
    path("wards/<int:pk>/",views.WardViewSet.as_view({"get": "retrieve","put": "update","patch": "partial_update","delete": "destroy"}),name="ward-detail"),
    path("provinces/<int:province_id>/districts/",views.districts_by_province,name="districts-by-province"),  
    path("districts/<int:district_id>/municipalities/",views.municipalities_by_district,name="municipalities-by-district"),
    path("municipalities/<int:municipality_id>/wards/",views.wards_by_municipality,name="wards-by-municipality"),
    
    path('farmers/', FarmerViewSet.as_view({'get': 'list', 'post': 'create'}), name='farmer-list'),
    path('farmers/<int:pk>/', FarmerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='farmer-detail'),
    
    path('lands/', LandViewSet.as_view({'get': 'list', 'post': 'create'}), name='land-list'),
    path('lands/<int:pk>/', LandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='land-detail'),
    
    path('crops/', CropViewSet.as_view({'get': 'list', 'post': 'create'}), name='crop-list'),
    path('crops/<int:pk>/', CropViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='crop-detail'),
    
    path('productions/', CropProductionViewSet.as_view({'get': 'list', 'post': 'create'}), name='production-list'),
    path('productions/<int:pk>/', CropProductionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='production-detail'),
    
    path('inventory/', InventoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='inventory-detail'),

    path('livestock/', LivestockViewSet.as_view({'get': 'list', 'post': 'create'}), name='livestock-list'),
    path('livestock/<int:pk>/', LivestockViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='livestock-detail'),

    path('soil-reports/', SoilReportViewSet.as_view({'get': 'list', 'post': 'create'}), name='soilreport-list'),
    path('soil-reports/<int:pk>/', SoilReportViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='soilreport-detail'),

    path('sales/', SaleViewSet.as_view({'get': 'list', 'post': 'create'}), name='sale-list'),
    path('sales/<int:pk>/', SaleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='sale-detail'),

    path('crop-diseases/', CropDiseaseViewSet.as_view({'get': 'list', 'post': 'create'}), name='cropdisease-list'),
    path('crop-diseases/<int:pk>/', CropDiseaseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='cropdisease-detail'),

    path('weather/', WeatherDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='weatherdata-list'),
    path('weather/<int:pk>/', WeatherDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='weatherdata-detail'),

    path('recommendations/', RecommendationViewSet.as_view({'get': 'list', 'post': 'create'}), name='recommendation-list'),
    path('recommendations/<int:pk>/', RecommendationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='recommendation-detail'),

    path('notifications/devices/', DeviceTokenListView.as_view(), name='device-list-create'),
    path('notifications/users/', UserDropdownListView.as_view(), name='user-dropdown-list'),
    
    # Trigger functions
    path('notifications/broadcast/', BroadcastNotificationView.as_view(), name='send-broadcast'),
    path('notifications/test-single/', TestNotificationView.as_view(), name='send-test-single'),
   
]

router = DefaultRouter()

router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"chalani", views.ChalaniViewSet, basename="chalani")

router.register(r"kotha-number", views.KothaNumberViewSet, basename="kotha-number")

router.register(r"aarthik-barsa", views.AarthikBarsaViewSet, basename="aarthik-barsa")

urlpatterns += router.urls

