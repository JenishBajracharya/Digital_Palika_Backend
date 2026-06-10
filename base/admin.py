from django.contrib import admin

from .models import (
    MainCategory,
    MahilaIdentityCard,
    BalbalikaIdentityCard,
    ApangaIdentityCard,
)


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
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
