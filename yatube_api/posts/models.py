from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    '''Модель создания групп постов.'''
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='адресная строка')
    description = models.TextField(verbose_name='описание')

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    '''Модель создания постов пользователей.'''
    text = models.TextField(verbose_name='Текст статьи')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор статьи')
    image = models.ImageField(upload_to='posts/', null=True, blank=True,
                              verbose_name='Картинка статьи')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              related_name='posts', blank=True, null=True,
                              verbose_name='Группа статей')

    def __str__(self):
        return self.text


class Comment(models.Model):
    '''Модель создания комментариев.'''
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Имя автора')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Имя поста')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True, db_index=True,
                                   verbose_name='Дата комментария')


class Follow(models.Model):
    '''Модель создания подписок.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Подписчик')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following',
                                  verbose_name='Автор поста')
