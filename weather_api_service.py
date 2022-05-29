# -*- coding: utf-8 -*-
import os
from requests import get


def get_weather(query: tuple[str, str]) -> dict:
    response = get(f'https://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}'
                            f'&q={",".join(query)}&lang=ru')
    return dict(response.json())
