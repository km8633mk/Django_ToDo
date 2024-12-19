from django.contrib import admin
from .models import Profile, Event, Photo, PackingItem, Message, Friendship, FriendRequest

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(PackingItem)
admin.site.register(Message)
admin.site.register(Friendship)
admin.site.register(FriendRequest)

