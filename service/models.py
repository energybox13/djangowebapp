from django.db import models

class cric_stats(models.Model): 
    player_name=models.CharField(max_length=50)
    fiftees=models.IntegerField()
    hundreds=models.IntegerField()
    wickets=models.IntegerField()
    average=models.FloatField()
    photo = models.ImageField(upload_to="media_main/", default="media_main/defaut.jpg")
    video=models.FileField(upload_to ="media_main", default="media_main/defaut.mp4")


class calc_user(models.Model):
    user=models.CharField(max_length=15)
    feedback=models.TextField()




