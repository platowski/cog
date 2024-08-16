from fastapi import APIRouter

from application.use_case.get_current_weather_for_city import GetCurrentWeatherForCity
from ports.into.weather import SupportedCities, CurrentWeather


router = APIRouter(
    prefix="/weather",
)


@router.get("/cities")
async def get():
    return {"cities": [city.value for city in SupportedCities]}


@router.get("/current/{city}", response_model=CurrentWeather)
async def get_current_for_city(city: SupportedCities):  # a bit too simple for pydantic model
    return await GetCurrentWeatherForCity.execute(city)
