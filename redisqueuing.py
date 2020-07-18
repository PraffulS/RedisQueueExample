from redis import Redis
from rq import Queue

from mars import get_mars_photo

q = Queue(connection=Redis())

def get_async_photos():
    for i in range(10):
        res = q.enqueue(get_mars_photo, 990 + i)
        print (res)