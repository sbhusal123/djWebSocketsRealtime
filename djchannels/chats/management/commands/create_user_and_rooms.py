from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User

from chats.models import Room

class Command(BaseCommand):
    help = "Create a custom user with chat rooms."


    def handle(self, *args, **kwargs):
        user_1 = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password": "thepassword",
            "is_staff": True,
            "is_superuser": True            
        }

        user_2 = {
            "username": "user2",
            "email": "user2@gmail.com",
            "password": "thepassword",
            "is_staff": True,
            "is_superuser": True
        }

        room = None
        try:
            # create user
            user1_obj, _ = User.objects.get_or_create(**user_1)
            user1_obj.set_password(user_1["password"])
            user1_obj.save()

            user2_obj, _ = User.objects.get_or_create(**user_2)
            user2_obj.set_password(user_1["password"])
            user2_obj.save()

        except Exception as e:
            pass

        room, _ = Room.objects.get_or_create(
            user1=User.objects.get(username=user_1["username"]),
            user2=User.objects.get(username=user_2["username"])
        )
        
        print("\n"*2)
        print("User1 Credentials")
        print("-"*150)
        print(user_1)
        print("-"*150)

        print("\n"*2)
        print("User2 Credentials")
        print("-"*150)
        print(user_2)
        print("-"*150)

        print("\n"*2)
        print("Authenticate separate user on incognito at::")
        print("-"*150)
        print(f"Login To: http://localhost:8000/admin")
        print("-"*150)



        print("\n"*2)
        print("Chat Room Link:")
        print("-"*150)
        print(f"http://localhost:8000/rooms/{room.pk} \nBefore Please Login To: http://localhost:8000/admin")
        print("-"*150)

        print("\n"*2)
