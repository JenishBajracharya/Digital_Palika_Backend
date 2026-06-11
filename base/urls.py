from django.urls import path

from . import views


urlpatterns = [
    path("categories/", views.category_list, name="category-list"),
    path("categories/<int:category_id>/form/", views.category_form, name="category-form"),
    path("darta/", views.DartaListCreateView.as_view(), name="darta-list-create"),
    path("darta/<int:pk>/", views.DartaDetailView.as_view(), name="darta-detail"),
    path("pariyojana/", views.PariyojanaListCreateView.as_view(), name="pariyojana-list-create"),
    path("pariyojana/<int:pk>/", views.PariyojanaDetailView.as_view(), name="pariyojana-detail"),
    path("rayak-no/", views.RayakNoListCreateView.as_view(), name="rayak-no-list-create"),
    path("rayak-no/<int:pk>/", views.RayakNoDetailView.as_view(), name="rayak-no-detail"),
]
