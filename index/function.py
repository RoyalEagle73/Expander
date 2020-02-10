import requests


def func(name):
    return requests.get(name).url
