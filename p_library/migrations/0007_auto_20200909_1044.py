# Generated by Django 2.2.6 on 2020-09-09 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20200908_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='Год рожения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=256, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=13, verbose_name='Международный стандартный книжный номер'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_books', to='p_library.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(verbose_name='Число копий'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Аннотация'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_release',
            field=models.SmallIntegerField(verbose_name='Год издания'),
        ),
    ]
