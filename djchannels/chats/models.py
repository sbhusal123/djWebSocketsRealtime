from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Room(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return f"<Room: {self.id}> {self.user1}, {self.user2}"
    
    # TODO: Implement custom logics for limitations

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"<Message: {self.user}>, {self.room}"
