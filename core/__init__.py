import json

from core.resources import UserDomain, UserAgent

from core.recon.domain_available import DomainAvailable as domain_availability
from core.recon.dns_history import DnsHistory as domain_host_history
from core.parser import ColorPrint
from core.recon.services.dnslg import DnsLG as DnsInformation


def index_in_list(a_list, index):
    return index < len(a_list)


def print_table(table_data):
    if isinstance(table_data, dict):
        table_data = table_data["records"]
        print(table_data)
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


def dict_to_table(dict_data):
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


def ProcessRequest():
    domain = UserDomain.DOMAIN

    ColorPrint.print_bold("Printing Results for domain %s" % domain)

    is_domain_available = domain_availability(domain)
    response = is_domain_available.domain_available
    if isinstance(response, bool):
        if response:
            _info = "Domain Available"
        else:
            _info = "Domain is Registered"
    else:
        _info = "unable to find result."

    ColorPrint.print_info("\nDomain Availability Result for %s : %s\n" % (domain, _info))

    dns_history = domain_host_history(domain)
    __domain_history = json.loads(dns_history.domain_history)

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

    dns_information = DnsInformation(domain)
    dns_records = dns_information.get_report()

    for dns_record in dns_records:
        record = dns_records[dns_record]
        print("")
        ColorPrint.print_info(record["title"])

        records = record["records"]

        print_table(dict_to_table(records))


__all__ = ["UserDomain", "UserAgent", "ProcessRequest", "DnsInformation"]
