import os

def validate_image_size(value):
    from django.core.exceptions import ValidationError
    filesize = value.size
    
    # Limit to 5MB
    if filesize > 5 * 1024 * 1024:
        raise ValidationError("图片大小不能超过 5MB")

from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name="吐槽内容")
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name="配图", validators=[validate_image_size])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    is_admin = models.BooleanField(default=False, verbose_name="是否管理员发布")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "吐槽"
        verbose_name_plural = "吐槽列表"

    def __str__(self):
        return self.content[:50]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="所属吐槽")
    content = models.TextField(verbose_name="评论内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    is_admin = models.BooleanField(default=False, verbose_name="是否管理员评论")

    class Meta:
        ordering = ['created_at']
        verbose_name = "评论"
        verbose_name_plural = "评论列表"

    def __str__(self):
        return self.content[:50]
