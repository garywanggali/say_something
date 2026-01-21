from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name="吐槽内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

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

    class Meta:
        ordering = ['created_at']
        verbose_name = "评论"
        verbose_name_plural = "评论列表"

    def __str__(self):
        return self.content[:50]
