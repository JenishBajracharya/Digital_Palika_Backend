from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


router = DefaultRouter()
router.register("categories", views.CategoryViewSet, basename="category")
router.register("janma-darta", views.JanmaDartaViewSet, basename="janma-darta")
router.register("mritu-darta", views.MrituDartaViewSet, basename="mritu-darta")
router.register("biwaha-darta", views.BiwahaDartaViewSet, basename="biwaha-darta")
router.register("migration-suchana", views.MigrationSuchanaViewSet, basename="migration-suchana")
router.register("file-bhitra", views.FileBhitraViewSet, basename="file-bhitra")
router.register("file-prakar", views.FilePrakarViewSet, basename="file-prakar")
router.register("rayak-khand-no", views.RayakKhandNoViewSet, basename="rayak-khand-no")
router.register("rayak_khand_no", views.RayakKhandNoViewSet, basename="rayak-khand-no-legacy")
router.register("file-record", views.FileRecordViewSet, basename="file-record")
router.register("file-chalani", views.FileChalaniViewSet, basename="file-chalani")
router.register("darta", views.DartaViewSet, basename="darta")
router.register("pariyojana", views.PariyojanaViewSet, basename="pariyojana")
router.register("rayak-no", views.RayakNoViewSet, basename="rayak-no")
router.register("mahila-identity-cards", views.MahilaIdentityCardViewSet, basename="mahila-identity-card")
router.register("balbalika-identity-cards", views.BalbalikaIdentityCardViewSet, basename="balbalika-identity-card")
router.register("apanga-identity-cards", views.ApangaIdentityCardViewSet, basename="apanga-identity-card")
router.register("chalani", views.ChalaniViewSet, basename="chalani")
router.register("kotha-number", views.KothaNumberViewSet, basename="kotha-number")
router.register("aarthik-barsa", views.AarthikBarsaViewSet, basename="aarthik-barsa")


urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("auth/register/", views.RegisterView.as_view(), name="auth-register"),
    path("auth/login/", views.LoginView.as_view(), name="auth-login"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/", include("rest_framework.urls")),
]
