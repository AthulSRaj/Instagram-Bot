from instagrapi import Client
import time

cl = Client()

cl.login('arthurrajking', 'Qwerty@1234')
friend_username = 'mariolaynefabrizio'

user_id = cl.user_id_from_username(friend_username)

medias = cl.user_medias(user_id, 5)

for media in medias:
    cl.media_like(media.id)
    cl.media_comment(media.id, "wow, I'm on acid and this is wild")
    print(f"Liked and commented on post: {media.pk}")
    time.sleep(20)