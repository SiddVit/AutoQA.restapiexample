import sys
import requests
import logging

from configs.settings import BASE_URL, API_V1

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel('DEBUG')


class POSTCreate(object):
    def __init__(self):
        self.base_url = BASE_URL
        self.v_api = API_V1
        self.endpoint = 'create'
        self.headers = {'Content-Type': 'application/json', 'User-Agent': 'request'}
        self.url = self.base_url + self.v_api + self.endpoint

    """
    example body = {'name':'test','salary':'123','age':'23'}
    """

    def post_create(self, body):
        response = requests.request('POST', url=self.url, data=body, headers=self.headers)
        logger.debug('\nRequest post_create with params:' +
                     '\nurl: ' + str(self.url) +
                     '\nheaders: ' + str(self.headers) +
                     '\ndata: ' + str(body) +
                     '\n' +
                     '\nResponse code is: ' + str(response.status_code) + '\n' +
                     '\nResponse body is: ' + str(response.text) + '\n')
        return response
