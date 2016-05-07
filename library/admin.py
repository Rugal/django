from django.contrib import admin
from library.models import Book, Dvd, Libuser, Libitem
from datetime import datetime, timedelta
# Register your models here.

def renew(modeladmin, request, queryset):
    queryset.filter(checked_out=True).update(duedate=datetime.today()+timedelta(days=21))
renew.short_description = "Change duedate to 3 weeks from today’s date"




class DvdInline(admin.TabularInline):
    model = Dvd # This shows all fields of Book.
    exclude = ('last_chkout', 'date_acquired')
    extra = 0

class BookInline(admin.StackedInline):
    model = Book # This shows all fields of Book.
    fields = [('title', 'author'), 'duedate',] # Customizes to show only certain fields
    extra = 0

class LibuserAdmin(admin.ModelAdmin):
    fields = [('username'), ('first_name', 'last_name')]
    inlines = [BookInline, DvdInline]

class BookAdmin(admin.ModelAdmin):
    #fields = [('title', 'author', 'pubyr'), ('checked_out', 'itemtype', 'user', 'duedate'),'category']
    fieldsets = ( ('Item Info',{'fields':(('title', 'author'),('pubyr', 'itemtype'))}), ('Other Info', {'fields':('user', 'duedate', 'last_chkout')}) )
    list_display = ('title', 'borrower')
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user #Returns the user who has borrowed this book
        else:
            return ''

class DvdAdmin(admin.ModelAdmin):
    #fields = [('title', 'maker', 'pubyr'), ('instructor', 'checked_out', 'itemtype', 'user', 'duedate'),'rating']
    fieldsets = ( ('Item Info',{'fields':(('title', 'maker'),('pubyr', 'itemtype'))}), )
    list_display = ('title', 'rating', 'borrower')
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user.username + '  checked out' #Returns the user who has borrowed this book


admin.site.register(Book, BookAdmin)
admin.site.register(Dvd, DvdAdmin)
admin.site.register(Libuser, LibuserAdmin)
