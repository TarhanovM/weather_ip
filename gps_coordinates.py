# -*- coding: utf-8 -*-
import os
import json


def get_coordinates() -> tuple:
    """
    This function gets coordinates from console util and retrieves location.
    :return: The coordinates look like (32.1522, 64.5272)
    """
    try:
        stream = os.popen('curl -s ipinfo.io', 'r')
        user_ipinfo = stream.read()
        stream.close()
    except Exception as ex:
        print(ex)
        print('Please install the curl!')
        print('$ sudo apt update'
              '$ sudo apt upgrade'
              '$ sudo apt install curl')
    else:
        location = json.loads(str(user_ipinfo))['loc']
        coordinates = tuple(map(float, location.split(',')))
        return coordinates
