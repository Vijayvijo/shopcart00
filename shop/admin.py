<<<<<<< HEAD
from django.contrib import admin
from .models import *



"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
admin.site.register(Category,CategoryAdmin)
    
    """

admin.site.register(Category)
admin.site.register(Product)

=======
from django.contrib import admin
from .models import *



"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
admin.site.register(Category,CategoryAdmin)
    
    """

admin.site.register(Category)
admin.site.register(Product)

>>>>>>> e7df23b (second commit)
