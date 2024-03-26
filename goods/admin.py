from django.contrib import admin

from goods.models import Categories, Products, UnitsOfMeasurement, Status


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]


@admin.register(UnitsOfMeasurement)
class UnitsOfMeasurementAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount", "status", "category",
                    "contactPerson", "storageLocation", "contactPerson", "image"]
    list_editable = ["discount", ]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category", "status"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity", "unitsOfMeasurement",
        "storageLocation", "contactPerson",
        "status",
    ]
