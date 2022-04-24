# Generated by Django 4.0.4 on 2022-04-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='테그명')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 테그',
                'verbose_name_plural': '패스트캠퍼스 테그',
                'db_table': 'fastcampus_tag',
            },
        ),
    ]