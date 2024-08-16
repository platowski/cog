from enum import Enum

from pydantic import BaseModel


# oversimplified list of supported cities for the sake of the example
class SupportedCities(str, Enum):
    NEW_YORK = 'New York'
    SAN_FRANCISCO = 'San Francisco'
    CHICAGO = 'Chicago'
    LOS_ANGELES = 'Los Angeles'


class TemperatureUnit(str, Enum):
    CELSIUS = 'C'
    FAHRENHEIT = 'F'


class Temperature(BaseModel):
    value: int
    unit: TemperatureUnit


class CurrentWeather(BaseModel):
    city: SupportedCities
    temperature: Temperature
    conditions: str
