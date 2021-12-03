import json
from urllib.error import HTTPError

from core.resources import UserDomain, UserAgent
from core.parser import domain_for_md as UrlParser
from urllib.request import urlopen, Request
from urllib.parse import urlencode


class DomainAvailable:
    '''
    This class check if a domain is available or not. We are using mdchecker.com for collecting information
    from server.
    '''
    __ENDPOINT__ = "https://madchecker.com/api/domain/get-information"

    def __init__(self, domain: str = None):
        '''
        Init function for data initialization
        :param domain: domain name required for analysis
        :type domain: str
        '''
        if domain:
            self.__domain = domain
        else:
            self.__domain = UserDomain.domain

        self.__is_available = False

    @property
    def domain_available(self) -> bool:
        '''
        This function check domain availability from server, and return result.
        :return: True/ False / raise exception in case of failure
        :rtype: bool
        '''
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
                    'User-Agent': str(user_agent.user_agent()),
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
                # @TODO: Resolve this exception with tuple and let the main function decide
                raise KeyError("We are failed to find domain status from server. Please try again in few minutes.")
        except HTTPError as e:
            raise e
