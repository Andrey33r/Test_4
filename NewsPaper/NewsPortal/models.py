from django.db import models


class Author(models.Model):
    password = models.CharField('password', max_length=128)
    last_login = models.DateTimeField('last login', blank=True, null=True)

    is_active = True


class User(Author):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True)


class Category(models.Model):
    name = models.CharField(max_length=264, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, default=2, on_delete=models.CASCADE)
    title_article = models.CharField(max_length=150)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    count = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    text_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
