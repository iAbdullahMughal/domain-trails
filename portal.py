import json
import os
import argparse

from core.recon.domain_available import DomainAvailable as domain_availability
from core.recon.dns_history import DnsHistory as domain_host_history
from core.resources import UserDomain


def banner():
    banner_text = """
  -------------------------------------------------------------------------------
      ____                            _           ______              _  __     
     / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
    / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
   / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  ) 
  /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/  
  -------------------------------------------------------------------------------
    Domain Trails - domains footprints, reconnaissance & information gathering 
  -------------------------------------------------------------------------------                                                                              
    """
    return banner_text


def print_result():
    domain = UserDomain.DOMAIN

    print(banner())
    print("Printing Results for domain %s" % domain)

    is_domain_available = domain_availability(domain)
    response = is_domain_available.domain_available
    if isinstance(response, bool):
        if response:
            _info = "Domain Available"
        else:
            _info = "Domain is Registered"
    else:
        _info = "unable to find result."

    print("\nDomain Availability Result for %s : %s\n" % (domain, _info))

    dns_history = domain_host_history(domain)
    __domain_history = json.loads(dns_history.domain_history)

    if __domain_history:
        print("DNS History Records")
        table_data = [
            [
                "Old Web Host", "New Web Host", "Month / Year", "Zone Date", "Transaction"
            ]
        ]
        for row in __domain_history:
            table_data.append(
                [
                    row["old_web_host"],
                    row["new_web_host"],
                    row["month_year"],
                    row["zone_date"],
                    row["transaction"],
                ]
            )
        col_width = max(len(word) for row in table_data for word in row) + 2  # padding
        separator = "-" * (col_width - 2)
        table_data.insert(
            1,
            [
                separator,
                separator,
                separator,
                separator,
                separator,
            ]
        )
        for row in table_data:
            print("".join(word.ljust(col_width) for word in row))


if __name__ == '__main__':
    os.system("")

    parser = argparse.ArgumentParser(description="Domain Trails, a project for domain information gathering from online"
                                                 "sources.")
    parser.add_argument("-d", dest="domain", required=True, type=str, help="Domain address for recon operation.")
    parser.add_argument("-p", dest="enable_proxy", type=bool, default=False,
                        help="Enable free ssl proxies while performing analysis.")
    args = parser.parse_args()

    if args.domain:
        UserDomain.DOMAIN = args.domain
    print_result()
