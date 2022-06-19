import click

from config import Config
from gps_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import Weather


@click.group('weather')
def cli():
    """The util gets your current weather"""
    config = Config()
    config.get_settings_path()


@cli.command('current')
def current_weather():
    """You'll get the current state of the weather"""
    config = Config()
    config.get_settings_path()
    config.initialize_variables()

    data_weather = None
    coordinates = get_coordinates()
    if coordinates:
        data_weather = get_weather(coordinates, Config())
    if data_weather:
        user_weather = Weather(data_weather)
        if getattr(config, 'FORMAT') == 'short':
            user_weather.weather_short_format()
        if getattr(config, 'FORMAT') == 'long':
            user_weather.weather_long_format()


@cli.command('api')
@click.argument('value', required=False)
def set_api_environment(value: str):
    """You can find out the api key if write without arguments.
    You can set api key if write with argument (short/long)"""
    config = Config()
    if value is not None:
        config.set_variable('API_KEY', value)
    click.echo(f'Your api key: {getattr(config, "API_KEY")}')


@cli.command('format')
@click.argument('value', required=False)
def set_api_environment(value: str):
    """You can find out the format if write without arguments.
    You can set format if write with argument (short/long)"""
    config = Config()
    if value is not None:
        if value.lower() in ('short', 'long'):
            config.set_variable('FORMAT', value)
            click.echo(f'Success!')
        else:
            click.echo(f'Invalid format!')
    else:
        click.echo(f'Your format: {getattr(config, "FORMAT")}')


cli.add_command(current_weather)
cli.add_command(set_api_environment)
