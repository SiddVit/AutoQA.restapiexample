import requests
import logging

from configs.settings import BASE_URL, API_V1


class GETEmployee(object):
    def __init__(self):
        self.base_url = BASE_URL
        self.v_api = API_V1
        self.endpoint = "employee/"
        self.headers = {'Content-Type': 'application/json', 'User-Agent': 'request'}
        self.url = self.base_url + self.v_api + self.endpoint

    """
    :param: id - id record's of employee
    """

    def get_employee(self, id_record):
        response = requests.request("GET", url=self.url + str(id_record), headers=self.headers)
        logging.warning("\nRequest get_employee with params:" +
                        "\nurl: " + str(self.url + str(id_record)) +
                        "\nheaders: " + str(self.headers) +
                        "\n" +
                        "\nResponse code is: " + str(response.status_code) + "\n" +
                        "\nResponse body is: " + str(response.text) + "\n")
        return response
