# Generated by Django 2.2.6 on 2020-09-08 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200902_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='pub',
        ),
        migrations.DeleteModel(
            name='PublishingHouse',
        ),
        migrations.AddField(
            model_name='book',
            name='redaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Redaction'),
        ),
    ]