import requests
from bs4 import BeautifulSoup
from seleniumbase import BaseCase

from get_forecast import GetForeCast

BaseCase.main(__name__, __file__)


class ComCast(BaseCase, GetForeCast):
    date_and_difference = None

    def test_scenario1(self):
        date_and_difference = self.get_current_date_and_days_difference(place="Kolkata", future_date="2023-02-05")
        print(f"Local Time: {date_and_difference.__getitem__(0)} Days Difference: {date_and_difference.__getitem__(1)}")

    def test_scenario2(self):
        date_and_difference = self.get_current_date_and_days_difference(place="Kolkata", future_date="2023-02-05")
        days = str(date_and_difference.__getitem__(1))
        key = "e45c365fbbdf4aec84e220319233101"
        city = "Chennai"
        req_url = f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days={days}&aqi=no&alerts=no"
        response = requests.get(req_url)
        data = response.content
        soup = BeautifulSoup(data, 'html.parser')
        print(soup.prettify())
