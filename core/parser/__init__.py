import sys

from core.parser.html_parser import DnsHistoryParser as HistoryWebParser


class UrlParser:
    """
    Class addresses cosmetic settings for an url. Different online services requires different shape of url so
    this class generally contains different function which beautify url/domain according to its requirement.
    """

    def __init__(self):
        """
        Setting url value to None
        """
        self.__url = None

    @property
    def url(self) -> str:
        """
        it returns url which was set before
        :return: domain / url
        :rtype: str
        """

        return self.__url

    @url.setter
    def url(self, u_url: str) -> None:
        """
        setter for url
        :param u_url: url as input of function
        :type u_url: str
        """
        self.__url = u_url

    @property
    def root_url(self) -> str:
        """
        This property function extracts root domain from given url

        :return: domain e.g. www.google.com
        :rtype: str
        """
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
        return url[0]


url_parser = UrlParser()


def domain_for_md(domain: str) -> str:
    """
    This function prepares domain for domain availability checking service.
    :param domain: takes input in any shape of urls e.g. http://www.example.com, https://www.example.com:8080
    :type domain: str
    :return: root of domain e.g. www.example.com
    :rtype: str
    """
    url_parser.url = domain
    domain = url_parser.root_url
    return domain


def domain_for_history(domain: str) -> str:
    """
    This function prepares domain for domain history checking service.
    :param domain: takes input in any shape of urls e.g. http://www.example.com, https://www.example.com:8080
    :type domain: str
    :return: simplified  domain e.g. example.com
    :rtype: str
    """
    url_parser.url = domain
    domain = url_parser.root_url
    if domain.startswith("www."):
        domain = domain.replace("www.", "")
    return domain


class ColorPrint:
    """
    This class provides support for color printing text in console.
    """

    @staticmethod
    def print_fail(message: str, end: str = '\n') -> None:
        """
        Print text in red color in console
        :param message: message which needs to be printed on console.
        :type message: str
        :param end: new line
        :type end: str
        :return: None
        :rtype: None
        """
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message: str, end: str = '\n') -> None:
        """
        Print text in green color in console
        :param message: message which needs to be printed on console.
        :type message: str
        :param end: new line
        :type end: str
        :return: None
        :rtype: None
        """

        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message: str, end: str = '\n') -> None:
        """
         Print text in warning color in console
        :param message: message which needs to be printed on console.
        :type message: str
        :param end: new line
        :type end: str
        :return: None
        :rtype: None
        """
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message: str, end: str = '\n') -> None:
        """
         Print text in green color in console
        :param message: message which needs to be printed on console.
        :type message: str
        :param end: new line
        :type end: str
        :return: None
        :rtype: None
        """
        sys.stdout.write('\x1b[1;34m' + "\n" + message.strip() + "\n" + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message: str, end: str = '\n') -> None:
        """
         Print text in bold format in console
        :param message: message which needs to be printed on console.
        :type message: str
        :param end: new line
        :type end: str
        :return: None
        :rtype: None
        """
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)


__all__ = ["HistoryWebParser", "domain_for_history", "ColorPrint", "domain_for_md"]
