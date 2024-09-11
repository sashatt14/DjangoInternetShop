from django.contrib import admin
from .models import Product,Review
class ProductAdmin(admin.ModelAdmin):
    pass
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProductAdmin)
admin.site.register(Review, ReviewAdmin)
