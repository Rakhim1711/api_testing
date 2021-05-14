

from api_testing.src.configs.hosts_configs import API_HOSTS
import requests
from api_testing.src.utilities.credentialUtility import CredentialUtility
import os
import pdb
import json
from requests_oauthlib import OAuth1
import logging as logger

class RequestsUtility(object):


    def __init__(self):

        wc_creds = CredentialUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])




    def post(self, endpoint, payload=None, headers=None, expected_status_code = 200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth = self.auth)

        import pdb; pdb.set_trace()
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code)
        logger.info(f'This test only passes if status code is {expected_status_code}, and not 200 !!!!!!!!!')

        return rs_api.json(


        )
        pdb.set_trace()








    def get(self):
        pass
