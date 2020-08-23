from django.contrib import admin
from TestApp.models import Enquiry, RC, Product, Feedback
# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display=["name","phone","email","issue","message"]


class RCAdmin(admin.ModelAdmin):
    list_display=["name","phone"]


class ProductAdmin(admin.ModelAdmin):
    list_display=["brand","products"]


class FeedbackAdmin(admin.ModelAdmin):
    list_display=["name","email","feedback"]


admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(RC,RCAdmin)
admin.site.register(Enquiry,EnquiryAdmin)
