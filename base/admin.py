from django.contrib import admin

from .models import *


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

@admin.register(Chalani)
class ChalaniAdmin(admin.ModelAdmin):

    list_display = (
        "chalani_no",
        "chalani_date",
        "letter_type",
        "receiving_branch",
        "receiver_name",
        "created_at",
    )

    search_fields = (
        "chalani_no",
        "subject",
        "receiver_name",
                "letter_type",
        "receiving_branch",
    )

    list_filter = (
        "letter_type",
        "receiving_branch",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(KothaNumber)
class KothaNumberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "kotha_no",
        "created_at",
    )

    search_fields = (
        "kotha_no",
    )

    ordering = (
        "kotha_no",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    
@admin.register(AarthikBarsa)
class AarthikBarsaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "aarthik_barsa",
        "created_at",
    )

    search_fields = (
        "aarthik_barsa",
    )

    ordering = (
        "aarthik_barsa",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )