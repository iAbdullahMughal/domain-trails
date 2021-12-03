import sys

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
    def root_url(self):
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
    domain = url_parser.root_url
    return domain


def domain_for_history(domain):
    url_parser.url = domain
    domain = url_parser.root_url
    if domain.startswith("www."):
        domain = domain.replace("www.", "")
    return domain


class ColorPrint:

    @staticmethod
    def print_fail(message, end='\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end='\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end='\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end='\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end='\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)


__all__ = ["HistoryWebParser", "domain_for_history", "ColorPrint"]
