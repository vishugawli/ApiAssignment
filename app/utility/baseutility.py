import requests
import pytest


class Baseutility(object):

    def response_generator(self, endpoint):
        url = "http://jsonplaceholder.typicode.com"+endpoint
        response = requests.get(url)
        data = response.json()

        return data

    @pytest.fixture(scope="session")
    def request_processor_user(self):
        user_data = self.response_generator("/users")
        user_details = {}
        for item in user_data:
            lat = int(float(item.get("address").get("geo").get("lat")))
            long = int(float(item.get("address").get("geo").get("lng")))

            if lat in range(-40, 5) and long in range(5, 100):
                user_details.update({str(item.get("id")): item.get("name")})

        return user_details

    @pytest.fixture(scope="session")
    def request_processor_todo(self):
        todo_data = self.response_generator("/todos")
        todo_details = {}
        for item in todo_data:
            if item.get("completed") is True:
                todo_details.update({str(item.get("id")): item.get("completed")})

        return todo_details

