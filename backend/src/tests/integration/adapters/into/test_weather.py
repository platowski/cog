import pytest

from ports.into.weather import SupportedCities, CurrentWeather


class TestWeatherAdapter:
    @pytest.mark.asyncio
    async def test_get_cities_returns_cities_collection(
        self, async_client
    ):
        async with async_client as ac:
            response = await ac.get(
                "/weather/cities"
            )
            assert response.status_code == 200
            result = dict(response.json())
            assert "cities" in result
            for city in result["cities"]:
                assert city in SupportedCities

    @pytest.mark.asyncio
    async def test_get_weather_returns_current_weather(
            self, async_client
    ):
        async with async_client as ac:
            response = await ac.get(
                "/weather/current/{}".format(SupportedCities.CHICAGO.value)
            )
            assert response.status_code == 200
            result = dict(response.json())
            weather = CurrentWeather(**result)
            assert weather.city == SupportedCities.CHICAGO.value

    @pytest.mark.asyncio
    async def test_get_weather_returns_error_for_unsupported_city_param(
            self, async_client
    ):
        async with async_client as ac:
            response = await ac.get(
                "/weather/current/{}".format("Never gonna give you up")
            )
            assert response.status_code == 422

