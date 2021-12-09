from domaintrails.core.resources import UserDomain

from domaintrails.core.recon.domain_available import DomainAvailable as DomainAvailability
from domaintrails.core.recon.dns_history import DnsHistory as DomainHostHistory
from domaintrails.core.parser import ColorPrint
from domaintrails.core.recon.dnslg import DnsLG as DomainDnsInformation
from domaintrails.core.resources import UserAgent
from domaintrails.core.recon.dbd_whois import DomainBigDataWhois


def index_in_list(a_list: list, index: int):
    '''
    This function is to check if some index exists inside a list.
    :param a_list: List of items
    :type a_list: list
    :param index: index pointer which needs be checked on list
    :type index: int
    :return: True / False
    :rtype: bool
    '''
    return index < len(a_list)


def print_table(table_data: list):
    '''
    We use this function to create table for printing information on console / terminal. We will be calculating
    column's information, separator and designing layout. After calculation this function will print information
    on terminal.
    :param table_data: table data in shape of list
    :type table_data: list
    '''

    sep_index = []
    for row in table_data:
        l_row = len(row)
        ptr_spe_index = 0
        while l_row:
            l_row = l_row - 1
            col_width = len(str(row[l_row])) + 2
            if index_in_list(sep_index, ptr_spe_index):
                stored_value = sep_index[ptr_spe_index]
                current_value = col_width
                if current_value > stored_value:
                    stored_value = current_value
                sep_index[ptr_spe_index] = stored_value
            else:
                sep_index.insert(
                    ptr_spe_index, col_width)

            ptr_spe_index = ptr_spe_index + 1
    separator_info = list(reversed(sep_index))
    separator_list = []
    for ptr_spe in separator_info:
        separator_list.append(
            "-" * (ptr_spe - 2)
        )

    table_data.insert(
        1, separator_list
    )
    for row in table_data:

        ptr_spe = 0
        output_line = ""
        for word in row:
            output_line = output_line + str(word).ljust(separator_info[ptr_spe])
            ptr_spe = ptr_spe + 1

        print(output_line)


def dict_to_table(dict_data: dict):
    '''
    This function converts dictionary data into list. This function is normally used to prepare data before printing
    on console/ terminal.
    :param dict_data: dictionary based data from different sources
    :type dict_data: dict
    :return: list based data is returned to caller
    :rtype: list
    '''
    table_data = []
    t_keys = []
    for row in dict_data:
        t_keys = list(row.keys())
        table_data.append(list(row.values()))
    update_key = []
    for key in t_keys:
        update_key.append(str(key).title().replace("_", " "))
    table_data.insert(0, t_keys)
    return table_data


def repair_keys(key):
    if "_" in key:
        key = str(key).replace("_", " ")
    return key.title()


def dict_to_list(dict_data, custom_header=None):
    list_data = []
    if "Useful_Information" in custom_header:
        custom_header = None
    for key in dict_data:
        data_key = repair_keys(key)
        if custom_header:
            data_key = custom_header + "  " + data_key
        list_data.append(
            [
                data_key,
                dict_data[key]
            ]
        )
    return list_data


def process_request(domain: str = None):
    '''
    This function is responsible for calling all the configured module and services in project. Following services are
    called by the function,
    1. DomainAvailability
    2. DomainHostHistory
    3. DomainDnsInformation

    Function later calls printing function to display all content

    '''
    if domain:
        UserDomain.domain = domain
    domain = UserDomain.domain

    ColorPrint.print_bold("Printing Results for domain %s" % domain)

    is_domain_available = DomainAvailability(str(domain))
    response = is_domain_available.domain_available
    if isinstance(response, bool):
        if response:
            _info = "Domain Available"
        else:
            _info = "Domain is Registered"
    else:
        _info = "unable to find result."
    ColorPrint.print_info("\x1b[6;30;42mDomain Availability Result for %s : %s\x1b[0m" % (domain, _info))

    dns_history = DomainHostHistory(str(domain))
    __domain_history = dns_history.domain_history()

    if __domain_history:

        ColorPrint.print_info("\x1b[6;30;42mDNS History Records\x1b[0m")
        # '\x1b[6;33;40m' + "Historical Record Number" + '\x1b[0m',
        table_data = [
            [
                "Old Web Host",
                "New Web Host",
                "Month / Year",
                "Zone Date",
                "Transaction",
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
        print_table(table_data)

    dns_information = DomainDnsInformation(str(domain))
    dns_records = dns_information.download_report()

    ColorPrint.print_info("\x1b[6;30;42mPrinting DNS Records Related To Domain\x1b[0m")
    for dns_record in dns_records:
        try:
            record = dns_records[dns_record]
            ColorPrint.print_info(" " + record["title"])

            records = record["records"]
            print_table(dict_to_table(records))
        except TypeError:
            # @TODO: Check which kind of records are failing while converting into table and printing process
            pass
    domain_bigdata_whois = DomainBigDataWhois()
    whois_data = domain_bigdata_whois.domain_whois()
    if whois_data:
        ColorPrint.print_info("\x1b[6;30;42mPrinting Whois Information\x1b[0m")
        whois_record = [
            ["Record Type", "Record Data"]
        ]
        for keys in whois_data.keys():
            title = keys.replace("_", " ").title()

            if keys in ["domain_record", "domain_registrant"]:
                for key in whois_data[keys]:
                    whois_record.append(
                        [
                            str(key).replace("_", " ").title(),
                            whois_data[keys][key]
                        ]
                    )

            elif keys == "host_records":
                for _keys in whois_data[keys]:
                    _title = str(_keys).replace("_", " ").upper()

                    print_table(whois_data[keys][_keys])

            elif keys == "domain_whois":
                for _keys in whois_data[keys]:
                    _child_data = whois_data[keys][_keys]
                    if isinstance(_child_data, str):
                        whois_record.append(
                            [
                                repair_keys(_keys),
                                _child_data
                            ]
                        )
                    elif isinstance(_child_data, dict):
                        _child_title = repair_keys(_keys)
                        record = dict_to_list(_child_data, _child_title)
                        whois_record = whois_record + record
            elif keys == "domain_whois_history":
                for _keys in whois_data[keys]:
                    _child_title = repair_keys(_keys)
                    h_whois = [
                        ['\x1b[6;33;40m' + "Historical Record Number" + '\x1b[0m',
                         '\x1b[6;33;40m%s\x1b[0m' % _child_title[-1]]
                    ]
                    _child_data = whois_data[keys][_keys]
                    if isinstance(_child_data, str):
                        print(_child_data)
                        h_whois.append(
                            [
                                repair_keys(_keys),
                                _child_data
                            ]
                        )
                    elif isinstance(_child_data, dict):
                        _child_title = repair_keys(_keys)
                        for _key in _child_data:
                            record = dict_to_list(_child_data[_key], _key)
                            h_whois = h_whois + record
                    print("\n")
                    print_table(h_whois)
            else:
                # @TODO: Check record information
                # print(keys)
                pass
        print("")
        print_table(whois_record)


__all__ = ["UserDomain", "UserAgent", "process_request", "DomainHostHistory", "DomainBigDataWhois"]
