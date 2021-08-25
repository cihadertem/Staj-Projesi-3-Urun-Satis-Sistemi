import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from user.models import CustomUser
from django.template.defaultfilters import time



class Room(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    first_user=models.ForeignKey(CustomUser,related_name="room_first",on_delete=models.CASCADE,null=True)
    second_user=models.ForeignKey(CustomUser,related_name="room_second",on_delete=models.CASCADE,null=True)
class Message(models.Model):
    user=models.ForeignKey(CustomUser,related_name="messages",verbose_name="Kullanıcı",on_delete=models.CASCADE)
    room=models.ForeignKey(Room,related_name="messages",verbose_name="Oda",on_delete=models.CASCADE)
    content=models.TextField(verbose_name="Mesaj İçeriği")
    created_date=models.DateTimeField(auto_now_add=True)
    what_is_it=models.CharField(max_length=50,null=True)


    def get_short_date(self):
        #return str(self.created_date.hour) + ":" + str(self.created_date.minute)
        return time(self.created_date, 'H:i')