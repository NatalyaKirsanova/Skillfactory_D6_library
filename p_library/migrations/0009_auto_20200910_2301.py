# Generated by Django 3.1.1 on 2020-09-10 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20200909_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='completion',
            field=models.NullBooleanField(default=None, verbose_name='Чтение завершено'),
        ),
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reader_books', to='p_library.reader', verbose_name='Читатель'),
        ),
        migrations.AddField(
            model_name='reader',
            name='address',
            field=models.CharField(default='', max_length=128, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Электронный адресс'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='redaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redaction_books', to='p_library.redaction', verbose_name='Редакция'),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Редакция'),
        ),
        migrations.DeleteModel(
            name='BookReading',
        ),
    ]