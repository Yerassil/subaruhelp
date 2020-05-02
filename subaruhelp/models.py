from django.db import models


class ObdCode(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField()

     @property
     def __str__(self):
         return self.title

class Comment(models.Model):
    obd_code = models.ForeignKey(ObdCode, on_delete=models.CASCADE)
    author = models.CharField('author', max_length=50)
    comment_text = models.TextField('comment text', max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    car_model = models.CharField('car model', max_length=50)

    def __str__(self):
        return '{}: {} ({})'.format(self.obd_code, self.author, self.car_model)
