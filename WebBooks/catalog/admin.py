from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

#admin.site.register(Author)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'borrower', 'id')
    list_filter = ('book', 'status', 'borrower')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'name_print', 'inv_num')
        }),
        ('Статус и окончание действия', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
