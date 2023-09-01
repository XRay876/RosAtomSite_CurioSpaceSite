# Generated by Django 4.2.2 on 2023-07-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_reportcomments_delete_reportcommentnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCommentsNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uProductIDReport', models.CharField(max_length=50, verbose_name='ID Продукта')),
                ('uVehIDReport', models.CharField(max_length=50, verbose_name='ID Вехи')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]