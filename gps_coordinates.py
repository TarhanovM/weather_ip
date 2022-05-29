# -*- coding: utf-8 -*-
import os
import json


def get_coordinates() -> tuple:
    stream = os.popen('curl -s ipinfo.io', 'r')
    user_ipinfo = stream.read()
    stream.close()
    coordinates = json.loads(str(user_ipinfo))['loc']
    return coordinates
