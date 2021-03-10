import json
import requests
import re
from API_Testing.Python_API_Test.API_utils.configuration import Configuration


class ApiHelpers:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        Configuration.site_url = baseurl

    # Method for Get response for request with valid api key and parameters
    def get_method_with_parameters(self, api_parameter):
        response = requests.get(self.baseurl + api_parameter)
        if response.status_code == 200:
            api_response = json.loads(response.text)
        else:
            raise ValueError("Bad request!")
        return api_response

    # Get response for request and return response headers
    def get_method_header(self, api_parameter):
        response = requests.get(self.baseurl + api_parameter)
        if response.status_code == 200:
            return response.headers, response.elapsed.total_seconds()
        else:
            raise ValueError("Bad request!")

    # Method for Get response for request with no/ invalid api key
    def get_method_no_apikey(self, api_parameter):
        response = requests.get(self.baseurl + api_parameter)
        if response.status_code == 401:
            api_response = json.loads(response.text)
        else:
            raise ValueError("Not expected status code")
        return api_response

    # Helper method for checking the url for Poster
    @staticmethod
    def check_url(url_str):
        # Regex to check valid URL
        regex = ("((http|https)://)" +
                 "m.media-amazon.com/" +
                 "images/" +
                 "M/" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.(?:jpg|gif|png)"
                 )

        # Compile the ReGex
        p = re.compile(regex)

        # Check the string matches the ReGex
        if re.search(p, url_str):
            return True
        else:
            return False

    # Helper method for checking the year format
    @staticmethod
    def check_year(year_str):
        # Regex to check valid year
        regex = "(\\b[0-9]{4}(-)*(\\b[0-9]{4})*)"

        # Compile the ReGex
        p = re.compile(regex)

        # Check the string matches the ReGex
        if re.search(p, year_str):
            return True
        else:
            return False
