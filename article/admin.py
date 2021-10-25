from .models import Comment
from django.contrib import admin

# Register your models here.
from .models import Article_Info, Section, Comment


class ArticleLink(admin.ModelAdmin):
    list_display = ['title', 'type_section', 'owner']
    list_display_links = ['title', 'type_section', 'owner']
    search_fields = ['title']
    list_filter = ['type_section', 'title', 'owner']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Article_Info, ArticleLink)
admin.site.register(Section)
# admin.site.register(Comment)
admin.site.site_header = 'URI admin'
admin.site.site_title = 'URI admin'
