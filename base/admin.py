from django.contrib import admin

from .models import (
    MainCategory,
    SubCategory,
    Darta,
    Pariyojana,
    RayakNo,
    MahilaIdentityCard,
    BalbalikaIdentityCard,
    ApangaIdentityCard,
)


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "main_category")
    list_filter = ("main_category",)
    search_fields = ("name",)


class BaseIdentityCardAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = (
        "first_name",
        "last_name",
        "category",
        "created_at",
    )
    list_filter = ("category",)
    search_fields = (
        "first_name",
        "last_name",
        "father_first_name",
        "mother_first_name",
        "grandfather_first_name",
    )


@admin.register(MahilaIdentityCard)
class MahilaIdentityCardAdmin(BaseIdentityCardAdmin):
    list_display = BaseIdentityCardAdmin.list_display + ("mobile_no", "marital_status")
    list_filter = BaseIdentityCardAdmin.list_filter + ("marital_status",)


@admin.register(BalbalikaIdentityCard)
class BalbalikaIdentityCardAdmin(BaseIdentityCardAdmin):
    list_display = BaseIdentityCardAdmin.list_display + ("gender",)
    list_filter = BaseIdentityCardAdmin.list_filter + ("gender",)


@admin.register(ApangaIdentityCard)
class ApangaIdentityCardAdmin(BaseIdentityCardAdmin):
    list_display = BaseIdentityCardAdmin.list_display + (
        "mobile_no",
        "gender",
        "blood_group",
        "disability_severity",
    )
    list_filter = BaseIdentityCardAdmin.list_filter + ("gender", "blood_group")
    search_fields = BaseIdentityCardAdmin.search_fields + ("citizenship_no",)


@admin.register(Darta)
class DartaAdmin(admin.ModelAdmin):
    list_display = (
        "darta_number",
        "main_category",
        "darta_date",
        "pathaune",
        "subject",
        "created_at",
    )
    list_filter = ("main_category", "darta_date")
    search_fields = ("pathaune", "subject", "description", "kaifiyat")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Pariyojana)
class PariyojanaAdmin(admin.ModelAdmin):
    list_display = (
        "project_code",
        "project_name",
        "main_category",
        "sub_category",
        "project_date",
        "project_status",
        "created_at",
    )
    list_filter = ("main_category", "sub_category", "project_status", "project_date")
    search_fields = ("project_name", "project_code", "project_description", "project_location")
    readonly_fields = ("created_at", "updated_at")


@admin.register(RayakNo)
class RayakNoAdmin(admin.ModelAdmin):
    list_display = (
        "rayak_no",
        "main_category",
        "sub_category",
        "created_at",
    )
    list_filter = ("main_category", "sub_category")
    search_fields = ("rayak_no",)
    readonly_fields = ("created_at", "updated_at")


