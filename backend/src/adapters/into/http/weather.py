from fastapi import APIRouter
import python_weather

from ports.into.weather import SupportedCities, CurrentWeather, Temperature, TemperatureUnit


router = APIRouter(
    prefix="/weather",
)


@router.get("/cities")
async def get():
    return {"cities": [city.value for city in SupportedCities]}


@router.get("/current/{city}", response_model=CurrentWeather)
async def get_current_for_city(city: SupportedCities):  # a bit too simple for pydantic model
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)

        return CurrentWeather(
            city=city.value,
            temperature=Temperature(value=weather.temperature, unit=TemperatureUnit.CELSIUS),
            conditions=weather.description
        )
