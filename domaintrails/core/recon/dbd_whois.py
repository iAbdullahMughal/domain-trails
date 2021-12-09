import urllib
from urllib.request import Request, urlopen
from domaintrails.core.parser.domain_big_data_parser import DomainBigDataParser
from domaintrails.core.resources import UserAgent, UserDomain
from domaintrails.core.parser import domain_for_history as UrlParser


class DomainBigDataWhois:
    __END_POINT__ = 'https://domainbigdata.com/'

    def __init__(self, domain: str = None):

        if domain:
            self.__domain = domain
        else:
            self.__domain = UserDomain.domain

    def domain_whois(self):

        domain = UrlParser(self.__domain)

        endpoint_url = self.__END_POINT__ + "/" + domain
        request = Request(endpoint_url)
        user_agent = UserAgent()
        request.add_header('Connection', 'keep-alive')
        request.add_header('Cache-Control', 'max-age=0')
        request.add_header('DNT', '1')
        request.add_header('Upgrade-Insecure-Requests', '1')
        request.add_header('Accept-Language', 'en-US,en;q=0.9')
        request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                                     'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        request.add_header('User-Agent', str(user_agent.user_agent()))

        try:
            content = urlopen(request).read().decode("utf-8")

            history = DomainBigDataParser(content)
            report = history.parse()

        except Exception as e:
            print(e)
            return []
        return report
#
#
# obh = DomainBigDataWhois("www.ebryx.com")
# import json
#
# print(json.dumps(obh.domain_whois(), indent=2))
