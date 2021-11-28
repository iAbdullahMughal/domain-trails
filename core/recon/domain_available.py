import json
from urllib.error import HTTPError

from core.resources import UserDomain, UserAgent
from core.parser import domain_for_md as UrlParser
from urllib.request import urlopen, Request
from urllib.parse import urlencode


class DomainAvailable:
    __ENDPOINT__ = "https://madchecker.com/api/domain/get-information"

    def __init__(self, domain=None):
        if domain:
            self.__domain = domain
        else:
            self.__domain = UserDomain.DOMAIN

        self.__is_available = False

    @property
    def domain_available(self):
        domain = UrlParser(self.__domain)
        params = {
            "domain": domain
        }
        query_string = urlencode(params)
        endpoint_url = self.__ENDPOINT__ + "?" + query_string
        try:
            user_agent = UserAgent()
            endpoint_request = Request(
                endpoint_url,
                None,
                headers={
                    'User-Agent': str(user_agent.USER_AGENT),
                }
            )
            with urlopen(endpoint_request) as response:
                response_text = response.read()
                content = json.loads(response_text)
                if "domain" in content:
                    domain_details = content["domain"]
                    available = domain_details["available"]
                    if available:
                        return True
                    else:
                        return False
                raise KeyError("We are failed to find domain status from server. Please try again in few minutes.")
        except HTTPError as e:
            raise e
