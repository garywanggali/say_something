from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'created_at', 'comment_count')
    inlines = [CommentInline]
    search_fields = ('content',)

    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = "内容预览"

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = "评论数"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'post', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)

    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = "内容预览"
