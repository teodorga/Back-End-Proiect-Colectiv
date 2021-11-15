from django.db import models


# Create your models here.
# modificare

# Category Model
class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.title)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return 'Course: {} {}'.format(
            self.title,
            self.description)


class Tutorial(models.Model):
    video = models.FileField(upload_to='videos/')
    #categoryID = models.IntegerField()
    description = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tutorials')
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return 'Tutorial: {} {} {}'.format(
            self.id,
            self.video,
            #self.categoryID,
            self.description,
            #self.image
            )


class Rating(models.Model):
    stars = models.IntegerField()
    nrOfVotes = models.IntegerField()
    starsAverage = models.IntegerField()
    tutorial = models.OneToOneField(Tutorial, on_delete=models.CASCADE, related_name='rating')

    def __str__(self):
        return 'Rating: {} {} {}'.format(
            self.stars,
            self.nrOfVotes,
            self.starsAverage)


class Comment(models.Model):
    userName = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return '{}: {}'.format(self.userName, self.content)

#caca