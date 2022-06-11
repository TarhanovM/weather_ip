# -*- coding: utf-8 -*-
import os
from requests import get
from typing import Union, Type
from config import Config


def get_weather(query: tuple[float, float], config: Type[Config]) -> Union[dict, None]:
    """
    This function gets information from WeatherAPI.com in the form of a dict.
    :param query: These are the coordinates at which the request is made.
    :param config: This is instance config class.
    :return: It returns information about the weather or None if api key is invalid.
    """
    try:
        response = get(f'https://api.weatherapi.com/v1/current.json?key={config.API_KEY}'
                       f'&q={",".join(list(map(str, query)))}&lang=ru')
    except Exception as ex:
        print('Invalid API KEY!')
    else:
        return dict(response.json())
