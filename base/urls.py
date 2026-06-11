from django.urls import path

from . import views


urlpatterns = [
    path("categories/", views.category_list, name="category-list"),
    path(
        "categories/<int:category_id>/form/",
        views.category_form,
        name="category-form",
    ),
    path("janma-darta/", views.janma_darta_form.as_view({"get": "list", "post": "create"})),
    path("janma-darta/<int:pk>/", views.janma_darta_form.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    path("mritu-darta/", views.mrituDartaViewSet.as_view({"get": "list", "post": "create"})),
    path("mritu-darta/<int:pk>/", views.mrituDartaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("biwaha-darta/", views.biwahaDartaViewSet.as_view({"get": "list", "post": "create"})),
    path("biwaha-darta/<int:pk>/", views.biwahaDartaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("migration-suchana/", views.migration_suchanaViewSet.as_view({"get": "list", "post": "create"})),
    path("migration-suchana/<int:pk>/", views.migration_suchanaViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("file-bhitra/", views.fileBhitraViewSet.as_view({"get": "list", "post": "create"})),
    path("file-bhitra/<int:pk>/", views.fileBhitraViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("file-prakar/", views.file_prakarViewSet.as_view({"get": "list", "post": "create"})),
    path("file-prakar/<int:pk>/", views.file_prakarViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("rayak_khand_no/", views.rayak_khand_no_ViewSet.as_view({"get": "list", "post": "create"})),
    path("rayak_khand_no/<int:pk>/", views.rayak_khand_no_ViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("file-record/", views.file_recordViewSet.as_view({"get": "list", "post": "create"})),
    path("file-record/<int:pk>/", views.file_recordViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    path("file-chalani/", views.file_chalaniViewSet.as_view({"get": "list", "post": "create"})),
    path("file-chalani/<int:pk>/", views.file_chalaniViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]


