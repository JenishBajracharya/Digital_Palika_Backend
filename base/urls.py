from django.urls import path

from . import views


urlpatterns = [
    path("categories/", views.category_list, name="category-list"),
    path(
        "categories/<int:category_id>/form/",
        views.category_form,
        name="category-form",
    ),
]
