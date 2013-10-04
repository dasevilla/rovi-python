import hashlib
import time

import requests
from requests.auth import AuthBase


class MasheryAuth(AuthBase):
    """
    Adds ``apikey`` and ``sig`` query parameters to the request
    """

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def __call__(self, r):
        params = {
            'apikey': self.key,
            'sig': self._sig(),
        }
        r.prepare_url(r.url, params)

        return r

    def _sig(self):
        timestamp = int(time.time())

        m = hashlib.md5()
        m.update(self.key)
        m.update(self.secret)
        m.update(str(timestamp))

        return m.hexdigest()


class RoviApi(object):

    ROVI_API_BASE = 'http://api.rovicorp.com'

    def __init__(self, service, version, key, secret):
        self.service = service
        self.version = version

        session = requests.Session()
        session.auth = MasheryAuth(key, secret)
        self.session = session

    def request_url(self, resource):
        return '/'.join([self.ROVI_API_BASE, self.service, self.version, resource])

    def make_request(self, resource, params=None):
        """
        Performs the API request. Most methods are a wrapper around this one.
        """
        if params is None:
            params = {}

        url = self.request_url(resource)
        params['format'] = 'json'

        r = self.session.get(url=url, params=params)

        r.raise_for_status()

        return r


class RoviDataApi(RoviApi):

    def __init__(self, key, secret):
        super(RoviDataApi, self).__init__('data', 'v1', key, secret)
