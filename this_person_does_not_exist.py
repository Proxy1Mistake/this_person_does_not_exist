from requests import Session
from time import time

from .objects import *

class Data:
    _get = Session().get
    _url = 'https://this-person-does-not-exist.com/{}'.format

class ThisPersonDoesNotExist(Data):
    @classmethod
    def new(cls, gender: str = 'all', age: str = 'all', ethnicity: str = 'all') -> New | int:
        """
        this this function is designed to generate

        :param gender: all, male, female

        :param age: all, 12-18, 19-25, 26-35, 35-50, 50

        :param ethnicity: all, asian, black, white, indian, middle_eastern, latino_hispanic

        :return: integer or info image to json
        """
        _req = cls._get(url = cls._url(f'new?time={int(time().real)}&gender={gender}&age={age}&etnic={ethnicity}'))
        return _req.status_code if _req.status_code != 200 else New(**_req.json())

    @classmethod
    def get_img(cls, name: str) -> bytes:
        """
        this function is designed to get an image

        :param name: take in ThisPersonDoesNotExist().new().name

        :return: images
        """
        req = cls._get(url = cls._url(f'img/{name}'))
        with open(file = f'{name}.jpg', mode = 'wb') as record_file:
            record_file.write(req.content)
            record_file.close()
