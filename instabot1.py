from instagrapi import Client
import time

cl = Client()

cl.login('UserName', 'Password')
friend_username = 'mariolaynefabrizio'

user_id = cl.user_id_from_username(friend_username)

medias = cl.user_medias(user_id, 5)

for media in medias:
    cl.media_like(media.id)
    cl.media_comment(media.id, "wow, good job")
    print(f"Liked and commented on post: {media.pk}")
    time.sleep(20)
