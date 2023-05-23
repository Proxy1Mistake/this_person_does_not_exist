from random import choices, randint
from requests import Session
from fake_useragent import FakeUserAgent
from time import time
from .objects import *
class this_person_does_not_exist:
    def __init__(self):
        self.headers = {
            'user-agent': FakeUserAgent().random
        }
        self.session = Session()
        self.url = 'https://this-person-does-not-exist.com/{}'.format

    def new(self, gender: str = None, age: str = None, ethnicity: str = None):
        if gender == None: gender = 'all'
        else: gender = gender
        if age == None: age = 'all'
        else: age = age
        if ethnicity == None: ethnicity = 'all'
        else: ethnicity = ethnicity
        clock_time = int(time().real)
        req = self.session.get(url = self.url(f'new?time={clock_time}&gender={gender}&age={age}&etnic={ethnicity}'), headers = self.headers)
        return new(req.json()).new

    def get_img(self, name: str):
        req = self.session.get(url = self.url(f'img/{name}'), headers = self.headers)
        img = open(f'{name}.jpeg', 'wb')
        img.write(req.content)
        img.close()