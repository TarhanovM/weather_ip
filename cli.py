import click

from config import Config
from gps_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import weather_short_format


@click.group('weather')
def cli():
    """The util gets your current weather"""
    pass


@cli.command('current')
def current_weather():
    """You'll get the current state of the weather"""
    user_weather = None
    coordinates = get_coordinates()
    if coordinates:
        user_weather = get_weather(coordinates, Config())
    if user_weather:
        weather_short_format(user_weather)


@cli.command('api')
@click.argument('value', required=False)
def set_api_environment(value):
    """You can get and install api key"""
    if value is not None:
        setattr(Config(), 'API_KEY', value)
    click.echo(f'Your api key: {Config().API_KEY}')


cli.add_command(current_weather)
cli.add_command(set_api_environment)
