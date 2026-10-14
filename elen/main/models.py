from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/')
    about = models.TextField()
    twitter_profile = models.CharField(blank=True)
    instagram = models.CharField(blank=True)
    facebook = models.CharField(blank=True)


    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.owner.first_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    article_image = models.ImageField(upload_to="article_images/")
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_articles")


    def __str__(self):
        return self.title


