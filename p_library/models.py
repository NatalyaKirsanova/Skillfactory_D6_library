import uuid
from django.utils.translation import gettext as _
from django.db import models
from django.core import validators

class Author(models.Model):
    full_name = models.CharField(max_length=256, verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))
    def __str__(self):
        return self.full_name

class Redaction(models.Model):
    name = models.CharField(max_length=128,verbose_name=_("Редакция") )
    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=256, verbose_name = _("Имя"))
    address = models.CharField(max_length=128, verbose_name = _("Адрес"))
    email = models.EmailField(verbose_name = _("Электронный адресс"))
    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13, verbose_name=_("Международный стандартный книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Цена"))
    completion = models.BooleanField(null=True,default=None,verbose_name=_("Чтение завершено"))
    avatar = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(
        "p_library.Author",
        on_delete = models.CASCADE,
        verbose_name = _("Автор"),
        related_name = "autor_books")
    redaction = models.ForeignKey(
        "p_library.Redaction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name = _("Редакция"),
        related_name = "redaction_books")
    reader = models.ForeignKey(
        "p_library.Reader",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name = _("Читатель"),
        related_name = "reader_books")
    def __str__(self):
        return self.title


