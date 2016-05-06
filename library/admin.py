from django.contrib import admin
from library.models import Book, Dvd, Libuser, Libitem
# Register your models here.

admin.site.register(Book)
admin.site.register(Dvd)
admin.site.register(Libuser)
