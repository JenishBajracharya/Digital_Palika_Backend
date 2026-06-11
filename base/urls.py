from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  *


router = DefaultRouter()

router.register(
    r"categories",
    CategoryViewSet,
    basename="category"
)
router.register(
    r"chalani",
    ChalaniViewSet,
    basename="chalani"
)

router.register(
    r"kotha-number",
    KothaNumberViewSet,
    basename="kotha-number"
)

router.register(
    r"aarthik-barsa",
    AarthikBarsaViewSet,
    basename="aarthik-barsa"
)

urlpatterns = router.urls

