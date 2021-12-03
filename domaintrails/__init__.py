from domaintrails.core.resources import UserDomain, UserAgent

from domaintrails.core.recon.domain_available import DomainAvailable as DomainAvailability
from domaintrails.core.recon.dns_history import DnsHistory as DomainHostHistory
from domaintrails.core.parser import ColorPrint
from domaintrails.core.recon.dnslg import DnsLG as DomainDnsInformation


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


def process_request():
    '''
    This function is responsible for calling all the configured module and services in project. Following services are
    called by the function,
    1. DomainAvailability
    2. DomainHostHistory
    3. DomainDnsInformation

    Function later calls printing function to display all content

    '''
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

    ColorPrint.print_info("Domain Availability Result for %s : %s" % (domain, _info))

    dns_history = DomainHostHistory(str(domain))
    __domain_history = dns_history.domain_history()

    if __domain_history:
        ColorPrint.print_info("DNS History Records")
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
        print_table(table_data)

    dns_information = DomainDnsInformation(str(domain))
    dns_records = dns_information.download_report()

    for dns_record in dns_records:
        try:
            record = dns_records[dns_record]
            ColorPrint.print_info(record["title"])

            records = record["records"]
            print_table(dict_to_table(records))
        except TypeError:
            # @TODO: Check which kind of records are failing while converting into table and printing process
            pass


__all__ = ["UserDomain", "UserAgent", "process_request", "DomainHostHistory"]
