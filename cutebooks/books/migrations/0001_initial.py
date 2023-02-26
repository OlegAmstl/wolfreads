# Generated by Django 4.1.6 on 2023-02-03 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения автора', null=True, verbose_name='Дата рождения автора')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти автора', null=True, verbose_name='Дата смерти автора')),
                ('photo', models.ImageField(blank=True, help_text='Добавьте фото автора', null=True, upload_to='', verbose_name='Фото автора')),
                ('biography', models.TextField(help_text='Укажите биографию автора', max_length=10000, verbose_name='Биография автора')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите жанр книги', max_length=150, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название книги', max_length=150, verbose_name='Название книги')),
                ('description', models.TextField(help_text='Напишите аннотацию книги', verbose_name='Описание книги')),
                ('cover', models.ImageField(blank=True, help_text='Добавьте обложку книги', upload_to='books/', verbose_name='Обложка книги')),
                ('pub_date', models.CharField(help_text='Укажите дату публикации', max_length=50, verbose_name='Дата публикации')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='Дата добавления книги на сайт')),
                ('author', models.ManyToManyField(help_text='Укажите автора книги', to='books.author', verbose_name='Автор книги')),
                ('genre', models.ForeignKey(help_text='Укажите жанр книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
