
import requests


def get_weather(latitude, longitude):

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=" + str(latitude)
            + "&longitude=" + str(longitude)
            + "&current="
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "wind_speed_10m"
        )


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        data = response.json()


        return data


    except Exception as error:

        print("WEATHER ERROR:")
        print(error)


        # Safe fallback

        return {

            "current": {

                "temperature_2m": 25,

                "relative_humidity_2m": 60,

                "precipitation": 0,

                "wind_speed_10m": 5

            }

        }
