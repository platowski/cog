from ports.into.weather import SupportedCities, CurrentWeather, Temperature, TemperatureUnit
import python_weather


class GetCurrentWeatherForCity:

    @staticmethod
    async def execute(city: SupportedCities) -> CurrentWeather:
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            # fetch a weather forecast from a city
            weather = await client.get(city)

            return CurrentWeather(
                city=city.value,
                temperature=Temperature(value=weather.temperature, unit=TemperatureUnit.CELSIUS),
                conditions=weather.description
            )