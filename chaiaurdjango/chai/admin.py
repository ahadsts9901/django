from django.contrib import admin
from .models import ChaiVariety, ChaiReviews, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model=ChaiReviews
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'created_at')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin )
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)