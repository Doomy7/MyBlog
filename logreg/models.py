from django.db import models

# Create your models here.
#custom user model
class users(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    interests = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)

#article model
class articles(models.Model):
    aid = models.AutoField(primary_key=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=1000)
    category = models.CharField(max_length=30)
    likesNo = models.IntegerField()
    commentsNo = models.IntegerField()

#comment model
class comments(models.Model):
    aid = models.ForeignKey(articles, on_delete=models.CASCADE)
    uid = models.ForeignKey(users, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

#like model
class likes(models.Model):
    aid = models.ForeignKey(articles, on_delete=models.CASCADE)
    uid = models.ForeignKey(users, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("aid", "uid")

