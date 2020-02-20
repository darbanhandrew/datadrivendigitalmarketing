from django.db import models


# Create your models here.
class Channel(models.Model):
    channel_name = models.CharField(max_length=200)

    # ...
    def __str__(self):
        return self.channel_name


class Step(models.Model):
    step_name = models.CharField(max_length=200)
    step_order = models.IntegerField(default=0)

    def __str__(self):
        return self.step_name


class Content(models.Model):
    content_name = models.CharField(max_length=200)
    content_factor = models.IntegerField(default=0)

    def __str__(self):
        return self.content_name


class IdealCube(models.Model):
    ideal_cube_channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    ideal_cube_step = models.ForeignKey(Step, on_delete=models.CASCADE)
    ideal_cube_content = models.ForeignKey(Content, on_delete=models.CASCADE)
    ideal_cube_value = models.IntegerField(default=0)

    def __int__(self):
        return self.ideal_cube_value


class RealCube(models.Model):
    real_cube_channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    real_cube_step = models.ForeignKey(Step, on_delete=models.CASCADE)
    real_cube_content = models.ForeignKey(Content, on_delete=models.CASCADE)
    real_cube_value = models.IntegerField(default=0)
    real_cube_publish_date = models.DateTimeField(auto_now_add=True, blank=True)

    def _int__(self):
        return self.real_cube_value
