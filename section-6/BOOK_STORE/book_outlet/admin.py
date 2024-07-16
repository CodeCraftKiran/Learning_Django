from django.contrib import admin

from .models import books, Author,Address, Country

class booksAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author", )
    

# Register your models here.
admin.site.register(books, booksAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)