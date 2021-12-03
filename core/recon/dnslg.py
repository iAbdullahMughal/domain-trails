import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from core import UserDomain, UserAgent

from core.parser import domain_for_history as UrlParser
import concurrent.futures


class DnsLG:
    '''
    Information:
    This class collect information about all the dns services currently available for domain. Following is the list of
    dns classes which are covered as part of this dns,
    Classes
      a         -> Host Address (A records)
      cert      -> Certificate (CERT records)
      dhcid     -> DHCP Identifier (DHCID records)
      cname     -> Canonical Name (CNAME records)
      aaaa      -> Pv6 Host Address (AAAA records)
      dlv       -> DNSSEC Lookaside Validation record (DLV records)
      dname     -> Delegation name (DNAME records)
      dnskey    -> DNS Key record (DNSKEY records)
      ds        -> Delegation Signer (DS records)
      hinfo     -> Host Information (HINFO records)
      hip       -> Host Identity Protocol (HIP records)
      kx        -> Key eXchanger record (KX records)
      loc       -> Location record (LOC records)
      mx        -> Mail Exchange record (MX records)
      naptr     -> Name Authority Pointer (NAPTR records)
      ns        -> Name Servers (NS records)
      nsec       -> Next-Secure record (NSEC records)
      nsec3     -> NSEC record version 3 (NSEC3 records)
      nsec3param-> NSEC3 parameters (NSEC3PARAM records)
      opt       -> Option record (OPT records)
      talink    -> Trust Anchor LINK (TALINK records)
      tlsa      -> TLSA records
      txt       -> Text record (TXT records)
      ta        -> DNSSEC Trust Authorities (TA records)
      rrsig     -> Resource Records Signature (RRSIG records)
      soa       -> Start of Authority (SOA record)
      spf       -> Sender Policy Framework (SPF records)
      srv       -> Service Locator (SRV records)
      sshfp     -> SSH Public Key Fingerprint (SSHFP records)
    above classes are part of this service.
    '''

    __get_auth = False
    __accept_value = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avi' \
                     'f,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    def __init__(self, domain: str = None, get_authority: bool = False):
        '''
        Initiating and assigning dns object with domain information.
        :param domain: domain which will be analyzed for records collection.
        :type domain: str
        :param get_authority: want to store authority information, default disabled
        :type get_authority: bool
        '''
        self.__get_auth = get_authority
        if domain:
            self.__domain = UrlParser(domain)
        else:
            self.__domain = UrlParser(str(UserDomain.domain))

    def __add_auth__(self, content: dict, result: list) -> list:
        '''
        This function will extract authority information from json response. It will store only when
        function is set self.__get_auth=True else it will be ignored
        :param content: dict of records downloaded from server
        :type content:  dict
        :param result: list of records shared with function, data is stored in this list
        :type result: list
        :return: list of records
        :rtype: list
        '''
        if self.__get_auth:
            if "authority" in content:
                authorities = content["authority"]
                for authority in authorities:
                    record = {
                        "name": authority["name"],
                        "type": authority["type"],
                        "class": authority["class"],
                        "ttl": authority["ttl"],
                        "endpoint": self.__extract_rdata__(authority["rdata"]),
                    }
                    if record not in result:
                        result.append(record)
        return result

    def __add_answer__(self, content: dict) -> list:
        '''
        This function will parse the response from server. If we are answers against the query we will pass
        information for processing.
        :param content: dict content downloaded from server against domain
        :type content: dict
        :return: list of records
        :rtype: list
        '''
        result = []
        if "answer" in content:
            answers = content["answer"]
            if answers:
                for answer in answers:
                    r_data = self.__extract_rdata__(answer["rdata"])
                    if len(r_data) == 1:
                        r_data = r_data[0]
                    else:
                        r_data = r_data
                    record = {
                        "name": answer["name"],
                        "type": answer["type"],
                        "class": answer["class"],
                        "ttl": answer["ttl"],
                        "endpoint": r_data,
                    }
                    if record not in result:
                        result.append(record)
        return result

    @staticmethod
    def __extract_rdata__(rdata: str) -> list:
        '''
        This function extract data from strings and make it readable in lists for different classes.
        :param rdata: class endpoint data
        :type rdata: str
        :return: list of records found in endpoint
        :rtype: list
        '''
        contents = str(rdata).split(" ")
        if len(contents) > 1:
            if "v=spf" in contents[0].lower() or len(contents) == 2:
                return [rdata]
            elif len(contents) == 7:
                return [{
                    "primary_nameserver": contents[0],
                    "host_master_email": contents[1],
                    "serial_number": contents[2],
                    "refresh": contents[3],
                    "retry": contents[4],
                    "expire": contents[5],
                    "minimum_ttl": contents[6],
                }]
            else:
                # @TODO: Need to parse this type of classes for table
                pass

            return contents
        else:
            contents = [contents[0].replace('"', "")]
            return contents

    def __download_record__(self, endpoint, timeout=10):
        '''

        :param endpoint:
        :type endpoint:
        :param timeout:
        :type timeout:
        :return:
        :rtype:
        '''
        request = Request(endpoint)
        user_agent = UserAgent()
        request.add_header('Connection', 'keep-alive')
        request.add_header('Cache-Control', 'max-age=0')
        request.add_header('DNT', '1')
        request.add_header('Upgrade-Insecure-Requests', '1')
        request.add_header('Accept-Language', 'en-US,en;q=0.9')
        request.add_header('Accept', self.__accept_value)
        request.add_header('User-Agent', str(user_agent.user_agent()))
        try:
            content = urlopen(request, timeout=timeout).read()
            content = json.loads(content)
            result = self.__add_answer__(content)
            result = self.__add_auth__(content, result)
        except HTTPError:
            return {}
        return result

    def download_report(self) -> dict:
        '''
        This function create different threads by using multiprocessing, and it performs multiple api request from
        server, response is collected and parsed according usage. This function also slices data as per requirements
        we are ignoring different classes from api response.
        :return: a result dict is returned which contains records
        :rtype: dict
        '''
        dns_info = {
        }
        endpoints = [
            "http://www.dns-lg.com/us01/" + self.__domain + "/a ",
            "http://www.dns-lg.com/us01/" + self.__domain + "/cert",
            "http://www.dns-lg.com/us01/" + self.__domain + "/dhc" + "id",
            "http://www.dns-lg.com/us01/" + self.__domain + "/cname",
            "http://www.dns-lg.com/us01/" + self.__domain + "/aa" + "aa",
            "http://www.dns-lg.com/us01/" + self.__domain + "/dlv",
            "http://www.dns-lg.com/us01/" + self.__domain + "/d" + "name",
            "http://www.dns-lg.com/us01/" + self.__domain + "/dns" + "key",
            "http://www.dns-lg.com/us01/" + self.__domain + "/ds",
            "http://www.dns-lg.com/us01/" + self.__domain + "/h" + "info",
            "http://www.dns-lg.com/us01/" + self.__domain + "/hip",
            "http://www.dns-lg.com/us01/" + self.__domain + "/kx",
            "http://www.dns-lg.com/us01/" + self.__domain + "/loc",
            "http://www.dns-lg.com/us01/" + self.__domain + "/mx",
            "http://www.dns-lg.com/us01/" + self.__domain + "/na" + "ptr",
            "http://www.dns-lg.com/us01/" + self.__domain + "/ns",
            "http://www.dns-lg.com/us01/" + self.__domain + "/opt",
            "http://www.dns-lg.com/us01/" + self.__domain + "/n" + "sec3",
            "http://www.dns-lg.com/us01/" + self.__domain + "/n" + "sec3param",
            "http://www.dns-lg.com/us01/" + self.__domain + "/ta" + "link",
            "http://www.dns-lg.com/us01/" + self.__domain + "/t" + "lsa",
            "http://www.dns-lg.com/us01/" + self.__domain + "/txt",
            "http://www.dns-lg.com/us01/" + self.__domain + "/ta",
            "http://www.dns-lg.com/us01/" + self.__domain + "/rr" + "sig",
            "http://www.dns-lg.com/us01/" + self.__domain + "/soa",
            "http://www.dns-lg.com/us01/" + self.__domain + "/spf",
            "http://www.dns-lg.com/us01/" + self.__domain + "/srv",
            "http://www.dns-lg.com/us01/" + self.__domain + "/ssh" + "fp",
            "http://www.dns-lg.com/us01/" + self.__domain + "/n" + "sec"
        ]
        data = []
        with concurrent.futures.ThreadPoolExecutor(10) as executor:
            future_to_url = {executor.submit(self.__download_record__, url): url for url in endpoints}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    if result:
                        data.append(result)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
        for _record in data:
            for record in _record:
                if record["type"].lower() == "a":
                    if "a" not in dns_info:
                        dns_info["a"] = {
                            "title": "Parent Name Server records",
                            "records": [],
                        }
                    dns_info["a"]["records"].append(record)
                elif record["type"].lower() == "aaaa":
                    if "aaaa" not in dns_info:
                        dns_info["aaaa"] = {
                            "title": "IP v6 Records",
                            "records": [],
                        }
                    dns_info["aaaa"]["records"].append(record)

                elif record["type"].lower() == "ns":
                    if "ns" not in dns_info:
                        dns_info["ns"] = {
                            "title": "Local Name Server Records",
                            "records": [],
                        }
                    dns_info["ns"]["records"].append(record)
                elif record["type"].lower() == "mx":
                    if "mx" not in dns_info:
                        dns_info["mx"] = {
                            "title": "Mail eXchanger (MX) Records",
                            "records": [],
                        }
                    dns_info["mx"]["records"].append(record)
                elif record["type"].lower() == "soa":
                    if "soa" not in dns_info:
                        dns_info["soa"] = {
                            "title": "Start of Authority (SOA)",
                            "records": [],
                        }
                    dns_info["soa"]["records"].append(record["endpoint"])
                elif record["type"].lower() == "txt":
                    if "txt" not in dns_info:
                        dns_info["txt"] = {
                            "title": "Text Records",
                            "records": [],
                        }
                    dns_info["txt"]["records"].append(record)
                else:
                    # @TODO: Handle other famous classes for table output
                    pass
        return dns_info
