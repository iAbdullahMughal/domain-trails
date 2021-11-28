from core.parser.html_parser import DnsHistoryParser as HistoryWebParser


class UrlParser:

    def __init__(self):
        self.__url = None

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, u_url):
        self.__url = u_url

    @property
    def ROOT_URL(self):
        url = self.__url
        if str(url).startswith("https://"):
            url = str(url).replace("https://", "")
        if str(url).startswith("http://"):
            url = str(url).replace("http://", "")
        if ":" in url:
            content = str(url).split(":")
            if len(content) > 1:
                url = content[0]
            else:
                url = content
        if "/" not in url:
            return url
        url = url.split("/")
        if len(url) > 1:
            return url[0]
        return url


url_parser = UrlParser()


def domain_for_md(domain):
    url_parser.url = domain
    domain = url_parser.ROOT_URL
    return domain


def domain_for_history(domain):
    url_parser.url = domain
    domain = url_parser.ROOT_URL
    if domain.startswith("www."):
        domain = domain.replace("www.", "")
    return domain


__all__ = ["HistoryWebParser"]
