from random import choices, randint
from requests import Session
from fake_useragent import FakeUserAgent
from time import time

from .objects import *

class Data:
    _headers = {
        'user-agent': FakeUserAgent().random
    }
    _session = Session()
    _url = 'https://this-person-does-not-exist.com/{}'.format
    _time = int(time().real)

class ThisPersonDoesNotExist(Data):
    @classmethod
    def new(cls, gender: str = None, age: str = None, ethnicity: str = None) -> New | int:
        """
        this this function is designed to generate

        :param gender: all, male, female

        :param age: all, 12-18, 19-25, 26-35, 35-50, 50

        :param ethnicity: all, asian, black, white, indian, middle_eastern, latino_hispanic

        :return: integer or info image to json
        """
        _gender = gender if gender else 'all'
        _age = age if age else 'all'
        _ethnicity = ethnicity if ethnicity else 'all'
        _req = cls._session.get(url = cls._url(f'new?time={cls._time}&gender={_gender}&age={_age}&etnic={_ethnicity}'), headers = cls._headers)
        if _req.status_code == 200: return New(data = _req.json()).new
        else: return _req.status_code

    @classmethod
    def get_img(cls, name: str) -> bytes:
        """
        this function is designed to get an image

        :param name: take in ThisPersonDoesNotExist().new().name

        :return: images
        """
        req = cls._session.get(url = cls._url(f'img/{name}'), headers = cls._headers)
        img = open(f'{name}.jpg', 'wb')
        img.write(req.content)
        img.close()