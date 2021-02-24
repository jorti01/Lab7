import requests

class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        if object_instance.number % 2 == 0:
           response = requests.get(f"https://restcountries.eu/rest/v2/region/Europe")
           print(response.content)
        else:
            response = requests.get(f"https://restcountries.eu/rest/v2/region/Asia")
            print(response.content)
