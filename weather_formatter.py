# -*- coding: utf-8 -*-

def weather_short_format(weather: dict) -> None:
    """
    This function prints weather information.
    :param weather: It is information from services.
    :return: None
    """
    try:
        print('The current weather:')
        print(f"Condition:         {weather['current']['condition']['text']}")
        print(f"Temperature:       {weather['current']['temp_c']}")
        print(f"Wind, kph:         {weather['current']['wind_kph']}")
        print(f"Wind directional:  {weather['current']['wind_dir']}")
        print(f"Pressure, kPa:     {weather['current']['pressure_mb']}")
    except Exception as ex:
        print('Some error, please check your api key')