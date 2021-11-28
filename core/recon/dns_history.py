import urllib
from urllib.request import Request, urlopen
import urllib.parse
from core import UserDomain, UserAgent

from core.parser import HistoryWebParser, domain_for_history as UrlParser


class DnsHistory:
    __END_POINT__ = 'http://www.hosterstats.com/historicaldns.php'

    def __init__(self, domain=None):
        if domain:
            self.__domain = domain
        else:
            self.__domain = UserDomain.DOMAIN

    @property
    def domain_history(self):
        domain = UrlParser(self.__domain)
        params = {
            "domain": domain
        }
        query_string = urllib.parse.urlencode(params)
        endpoint_url = self.__END_POINT__ + "?" + query_string
        request = Request(endpoint_url)
        user_agent = UserAgent()
        request.add_header('Connection', 'keep-alive')
        request.add_header('Cache-Control', 'max-age=0')
        request.add_header('DNT', '1')
        request.add_header('Upgrade-Insecure-Requests', '1')
        request.add_header('Accept-Language', 'en-US,en;q=0.9')
        request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                                     'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        request.add_header('User-Agent', str(user_agent.USER_AGENT))

        try:
            content = urlopen(request).read()
            history = HistoryWebParser(content)
            report = history.report

        except Exception as e:
            raise e
        return report
