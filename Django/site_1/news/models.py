from django.db import models


class News(models.Model):
    title = models.CharField(max_length = 150 ,verbose_name="Наименования")
    content = models.TextField(blank=True,verbose_name="Контент")
    creat_up = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    update_up = models.DateTimeField(auto_now=True,verbose_name="Дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото",blank=True)
    is_publishen = models.BooleanField(default=True,verbose_name="Опубликовано?")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ["-creat_up"]
