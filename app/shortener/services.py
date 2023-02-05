import random 
import string

from .models import Url
host = 'http://127.0.0.1:8000/'


def get_random_string(size=6, chars=string.ascii_uppercase+string.ascii_lowercase+ string.digits)-> str:
    """returns string with 6 random elements"""
    return ''.join(random.choice(chars) for _ in range(size))


def create_url_object(original_url: str)-> None:
    '''takes original url, save Url in db with hash'''
    random_hash = get_random_string()
    url = Url(original_url=original_url, hash=random_hash)
    url.save()


def get_short_url(original_url: str)-> str:
    hash = Url.objects.get(original_url=original_url).hash
    return host + hash


def get_original_version(url_hash: str)-> str:
    return Url.objects.get(hash=url_hash).original_url
