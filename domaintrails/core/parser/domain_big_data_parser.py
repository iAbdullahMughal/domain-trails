from html.parser import HTMLParser

import re


class ParserHelper:

    @staticmethod
    def validate_email(email_address):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if "(at)" in email_address:
            email_address = str(email_address).replace("(at)", "@")

        if re.fullmatch(regex, email_address):
            return email_address
        else:
            # @TODO: Check if its not valid email address, need to create a log
            return email_address

    @staticmethod
    def known_fields(field, key_validation=True):
        field = ''.join([i for i in field if not i.isdigit()])
        field = field.lower()
        known_list = [
            "name",
            "organization",
            "email",
            "address",
            "city",
            "state",
            "country",
            "phone",
            "fax",
            "private",
        ]
        if field in known_list:
            return True
        else:
            known_ignore_list = [
                "registrant",
                "from last whois record",
                "redacted for privacy",
                "is associated with + domains",
                ", contact registrar for more details",
                "is associated with  domains",
                "map",
                "no",
            ]
            if key_validation:
                if field not in known_ignore_list:
                    # @TODO: Need to check what kind of data is found on domain big data website.
                    pass
            return False

    @staticmethod
    def redact_data(data):
        if "REDACTED FOR PRIVACY".lower() in str(data).lower():
            return None
        elif "Data protected, not disclosed".lower() in str(data).lower():
            return None
        else:
            return data

    @staticmethod
    def validate_phone_number(str_phone_number):
        phone_number = str_phone_number
        phone_number = str(phone_number).replace("+", "")
        phone_number = phone_number.replace(" ", "")
        phone_number = phone_number.replace(".", "")
        phone_number = phone_number.replace("-", "")
        phone_number = phone_number.replace("(", "")
        phone_number = phone_number.replace(")", "")

        for _char in phone_number:
            if _char.isalpha():
                return None
        return str_phone_number

    @staticmethod
    def whois_ignore_cases(record_line):
        if "Whois" == record_line:
            return True
        ignore_list = [
            "querying the whois server",
        ]

        for ignore_case in ignore_list:
            if ignore_case in record_line:
                return True
        return False

    @staticmethod
    def generate_data_tree(value, key, data, child_value=None, parent_value=None):
        key = key.lower()
        key = key.replace(value.lower(), "")
        if key.startswith(" "):
            key = key[1:]
            if not key:
                key = "name"
        if data.startswith(" "):
            data = " ".join(data.split())
        if key.startswith(" "):
            key = " ".join(key.split())
        if "http#//" in data:
            data = data.replace("http#//", "http://")
        if "https#//" in data:
            data = data.replace("https#//", "https://")
        if "(at)" in data:
            data = data.replace("(at)", "@")
        if not key:
            key = "name"
        if child_value:
            key = child_value
        parent = str(value).title()
        if parent_value:
            parent = parent_value
        return {
            "parent": parent.replace(" ", " "),
            "child": key.replace(" ", "_"),
            "data": data
        }

    @staticmethod
    def extract_data(record_line):
        record_line = record_line.rstrip().strip().replace("\t", " ")
        record_line = record_line.replace("http://", "http#//").replace("https://", "https#//")
        if ":" in record_line:
            list_of_records = record_line.split(":", 1)
            key, data = list_of_records[0], list_of_records[1]

            ignore_cases = [
                "dnssec",
                ">>> ",
                "NOTICE",
                "DNSSEC",
                "URL of the ICANN WHOIS Data Problem Reporting System",
                "only for lawful purposes and that",
                "Please note",
                "available at",
                "for more information on whois",
            ]
            for _key in ignore_cases:
                if _key in key:
                    return False, None
            if len(key) > 30:
                return False, None
            if "Registrar".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Registrar".lower(), key, data)
            elif "Domain".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Domain".lower(), key, data)
            elif "Registrant".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Registrant".lower(), key, data)
            elif "Name Server".lower() in key.lower() or "Nserver".lower() in key.lower() \
                    or "Nameservers".lower() in key.lower() or "DNS".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Name Server".lower(), key, data)
            elif "Tech".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Tech".lower(), key, data)
            elif "Billing".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Billing".lower(), key, data)
            elif "Trademark".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Trademark".lower(), key, data)
            elif "Admin".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Admin".lower(), key, data)
            elif "trouble".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Admin".lower(), key, data)
            elif "Reseller".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Reseller".lower(), key, data)
            elif "Organization".lower() in key.lower():
                return True, ParserHelper.generate_data_tree("Organization".lower(), key, data)
            elif "Domain Status".lower() in key.lower() or "Status".lower() in key.lower() and \
                    "whois" not in key.lower():
                return True, ParserHelper.generate_data_tree("Domain Status".lower(), key, data)
            elif "Updated Date".lower() in key.lower() or "Creation Date".lower() in key.lower() \
                    or "last modified" in key or "renewal date" in key or "Expiry date" in key:
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Date")

            elif " email".lower() in key.lower() or "Email".lower() in key.lower() or "e-mail".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " address".lower() in key.lower() or "address".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " Phone".lower() in key.lower() or "Phone".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " Fax".lower() in key.lower() or "Fax".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " contact".lower() in key.lower() or "contact".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " WHOIS Server".lower() in key.lower() or "WHOIS Server".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " country".lower() in key.lower() or "country".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " anonymous".lower() in key.lower() or "anonymous".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " changed".lower() in key.lower() or "changed".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")
            elif " Name".lower() in key.lower() or "Name".lower() in key.lower():
                return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                             parent_value="Useful_Information")

            elif "date" in key.lower() or "Created".lower() in key.lower() or "Expires".lower() in key.lower():
                if ">>>" not in key:
                    return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                                 parent_value="Date")
            elif "whois" in key.lower():
                pass
            else:

                if len(key) < 20:
                    return True, ParserHelper.generate_data_tree(value="", key="", data=data, child_value=key.lower(),
                                                                 parent_value="Useful_Information")

        else:
            if "date" in record_line.lower() and "clientUpdate".lower() not in record_line.lower():
                if len(record_line) < 50:
                    records = record_line.split()
                    return True, ParserHelper.generate_data_tree(value="", key="", data=records[1],
                                                                 child_value=records[0],
                                                                 parent_value="Date")
        return False, None

    @staticmethod
    def ext_table_data(web_content: str):
        """
        This function extracts tables from html content, it creates a list and append all extracted tables in it.
        :param web_content: string based html content
        :type web_content:  str
        :return html_tables, max_table_length: list of extracted tables, number of tables in table list
        :rtype html_tables, max_table_length: list, int
        """
        web_content = str(web_content)
        html_tables = []
        max_table_length = 0
        html_table_regex = r'<table.*?/table>'
        table_row_regex = r'<tr.*?/tr>'
        row_data_regex = r'<(td|th).*?/(td|th)>'
        found_tables = re.search(html_table_regex, web_content, re.DOTALL)
        while found_tables:
            table_record = found_tables.group()
            found_table_rows = re.search(table_row_regex, table_record, re.DOTALL)
            __table_record = []
            while found_table_rows:
                record_row = found_table_rows.group()  # the row
                record_row_data = re.search(row_data_regex, record_row, re.DOTALL)
                __row_record = []
                while record_row_data:
                    record_row_cell_data = record_row_data.group()
                    __row_record.append(record_row_cell_data.strip())
                    record_row = re.sub(row_data_regex, '', record_row, 1, re.DOTALL)
                    record_row_data = re.search(row_data_regex, record_row, re.DOTALL)
                __table_record.append(__row_record)
                if max_table_length < len(__row_record):
                    max_table_length = len(__row_record)
                table_record = re.sub(table_row_regex, '', table_record, 1, re.DOTALL)
                found_table_rows = re.search(table_row_regex, table_record, re.DOTALL)

            web_content = re.sub(html_table_regex, '', web_content, 1, re.DOTALL)
            html_tables.append(__table_record)
            found_tables = re.search(html_table_regex, web_content, re.DOTALL)
        return html_tables, max_table_length

    @staticmethod
    def generate_table(html_table):
        table_data = []
        for record_row in html_table:
            extract_row_record = []
            for record_column in record_row:
                data_value = re.findall(r'>(.+?)<', record_column)
                if isinstance(data_value, list):
                    data_value = data_value[0]
                if ">" in data_value:
                    data_value = str(data_value).split(">")[-1]
                extract_row_record.append(
                    data_value
                )
            table_data.append(extract_row_record)
        return table_data

    @staticmethod
    def extract_hostname_data(html):
        hostname_records = {}

        extracted_html_tables, max_len = ParserHelper.ext_table_data(html)
        for tables in reversed(extracted_html_tables):
            matched_value = re.findall(r'>(.+?)<', tables[0][0])
            if matched_value:
                matched_value = matched_value[0]
                if "MX" == matched_value:
                    hostname_records["mx"] = ParserHelper.generate_table(tables)
                    hostname_records["mx"].insert(0, [
                        "Type",
                        "Hostname",
                        "Address",
                        "Preference",
                        "TTL",
                        "Class",
                    ])

                elif "A" == matched_value:

                    hostname_records["a"] = ParserHelper.generate_table(tables)
                    hostname_records["a"].insert(0, [
                        "Type",
                        "Hostname",
                        "Address",
                        "TTL",
                        "Class",
                    ])
                elif "AAAA" == matched_value:
                    # print(tables)

                    hostname_records["aaaa"] = ParserHelper.generate_table(tables)
                    hostname_records["aaaa"].insert(0, [
                        "Type",
                        "Hostname",
                        "Address",
                        "TTL",
                        "Class",
                    ])
                elif "Date" == matched_value:
                    hostname_records["dns_history"] = ParserHelper.generate_table(tables)
        return hostname_records


class DomainInfoParser(HTMLParser):
    domain_record = {}
    row_counter = 0
    key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.row_counter = 0
        self.key = ""
        self.data = []
        self.domain_record = {
            "domain": None,
            "words_in": None,
            "ip_address": None,
            "ip_geo_location": None,
            "title": None,
            "date_creation": None,
            "web_age": None,
        }

    def handle_starttag(self, tag, attributes):
        if tag != 'div':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'id' and value == 'idCardWebsite':
                break
        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            extract_data = data
            extract_data = extract_data.strip().rstrip()
            if extract_data and " abuse reports" not in extract_data and "map" != extract_data:
                if not self.row_counter == 0:
                    if self.row_counter % 2 == 1:
                        if extract_data == "Domain":
                            self.key = "domain"
                        elif extract_data == "Words in":
                            self.key = "words_in"
                        elif extract_data == "IP Address":
                            self.key = "ip_address"
                        elif extract_data == "IP Geolocation":
                            self.key = "ip_geo_location"
                        elif extract_data == "Title":
                            self.key = "title"
                        elif extract_data == "Date creation":
                            self.key = "date_creation"
                        elif extract_data == "Web age":
                            self.key = "web_age"
                    else:
                        self.domain_record[self.key] = extract_data
                self.row_counter += 1


class DomainRegistrantParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.key = ""
        self.is_key = False
        self.data = []
        self.domain_registrant = {}

    def handle_starttag(self, tag, attributes):
        if tag != 'div':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'id' and value == 'MainMaster_divRegistrantIDCard':
                break
        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            extract_data = data
            extract_data = extract_data.strip().rstrip()
            if extract_data:
                if not self.is_key:

                    if ParserHelper.known_fields(extract_data):
                        self.key = extract_data
                        self.is_key = True
                else:
                    if self.key and self.is_key:
                        if not ParserHelper.known_fields(extract_data, False):
                            if ParserHelper.redact_data(extract_data):
                                if self.key.lower() == "email":
                                    email = ParserHelper.validate_email(ParserHelper.redact_data(extract_data))
                                    self.domain_registrant[self.key] = email
                                elif self.key.lower() == "phone":
                                    phone = ParserHelper.redact_data(extract_data)
                                    phone = ParserHelper.validate_phone_number(phone)
                                    if phone:
                                        self.domain_registrant[self.key] = phone
                                elif self.key.lower() == "fax":
                                    fax = ParserHelper.redact_data(extract_data)
                                    fax = ParserHelper.validate_phone_number(fax)
                                    if fax:
                                        self.domain_registrant[self.key] = fax
                                else:
                                    self.domain_registrant[self.key] = ParserHelper.redact_data(extract_data)
                            self.key = None
                            self.is_key = False
                        else:
                            self.key = extract_data
                            self.is_key = True


class DomainWhoIsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
        self.domain_whois = {}

    def handle_starttag(self, tag, attributes):
        if tag != 'div':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'id' and value == 'MainMaster_divWhois':
                break
        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            extract_data = data
            extract_data = extract_data.strip().rstrip()
            if extract_data:
                if not ParserHelper.whois_ignore_cases(extract_data):
                    if "last record, updated :" in extract_data:
                        extract_data = extract_data.replace("last record, updated :", "")
                        self.domain_whois["record_date"] = extract_data
                    elif "Domain Name:".lower() in extract_data.lower():
                        self.domain_whois["domain_name"] = extract_data.replace("Domain Name:", "")
                    elif "Registry Domain ID:".lower() in extract_data.lower():
                        self.domain_whois["registry_domain_id"] = extract_data.replace("Registry Domain ID:", "")
                    else:
                        status, content = ParserHelper.extract_data(extract_data)

                        if status:
                            parent_node, child_node, child_data = content["parent"], content["child"], content["data"]
                            if child_data:
                                if parent_node not in self.domain_whois:
                                    self.domain_whois[parent_node] = {}
                                if child_node not in self.domain_whois[parent_node]:
                                    self.domain_whois[parent_node][child_node] = None
                                if self.domain_whois[parent_node][child_node]:
                                    if isinstance(self.domain_whois[parent_node][child_node], str):
                                        previous_data = self.domain_whois[parent_node][child_node]
                                        self.domain_whois[parent_node][child_node] = [
                                            previous_data, content["data"]
                                        ]
                                    elif isinstance(self.domain_whois[parent_node][child_node], list):
                                        self.domain_whois[parent_node][child_node].append(child_data)
                                    else:
                                        self.domain_whois[parent_node][child_node] = child_data
                                else:
                                    self.domain_whois[parent_node][child_node] = child_data


class DomainWhoIsHistoryParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
        self.record_counter = 1
        self.domain_whois = {}
        self.current_record = ""

    def handle_starttag(self, tag, attributes):
        if tag != 'div':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'id' and value == 'divRptHistoryMain':
                break
        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            extract_data = data
            extract_data = extract_data.strip().rstrip()
            if extract_data:
                if not ParserHelper.whois_ignore_cases(extract_data):
                    status, content = ParserHelper.extract_data(extract_data)
                    if status:
                        parent_node, child_node, child_data = content["parent"], content["child"], content["data"]
                        if child_node == "recorded_":
                            self.current_record = "history_record_no_" + str(self.record_counter)
                            if self.current_record not in self.domain_whois:
                                self.domain_whois[self.current_record] = {}
                                self.record_counter += 1

                        if child_data:
                            if parent_node not in self.domain_whois[self.current_record]:
                                self.domain_whois[self.current_record][parent_node] = {}
                            if child_node not in self.domain_whois[self.current_record][parent_node]:
                                self.domain_whois[self.current_record][parent_node][child_node] = None
                            if self.domain_whois[self.current_record][parent_node][child_node]:
                                if isinstance(self.domain_whois[self.current_record][parent_node][child_node], str):
                                    previous_data = self.domain_whois[self.current_record][parent_node][child_node]
                                    self.domain_whois[self.current_record][parent_node][child_node] = [
                                        previous_data, content["data"]
                                    ]
                                elif isinstance(self.domain_whois[self.current_record][parent_node][child_node], list):
                                    self.domain_whois[self.current_record][parent_node][child_node].append(child_data)
                                else:
                                    self.domain_whois[self.current_record][parent_node][child_node] = child_data
                            else:
                                self.domain_whois[self.current_record][parent_node][child_node] = child_data


class DomainBigDataParser:

    def __init__(self, html_content=None):
        self.html_content = ""
        if html_content:
            self.html_content = html_content

    def parse(self, html_content=None):
        bigdata_record = {}
        if html_content:
            self.html_content = html_content
        domain_info_parser = DomainInfoParser()
        domain_info_parser.feed(self.html_content)
        domain_info = domain_info_parser.domain_record
        if domain_info:
            bigdata_record["domain_record"] = domain_info

        domain_registrant_parser = DomainRegistrantParser()
        domain_registrant_parser.feed(self.html_content)
        domain_registrant_parser = domain_registrant_parser.domain_registrant
        if domain_registrant_parser:
            bigdata_record["domain_registrant"] = domain_registrant_parser

        domain_whois_info = DomainWhoIsParser()
        domain_whois_info.feed(self.html_content)
        domain_whois_info = domain_whois_info.domain_whois
        if domain_whois_info:
            bigdata_record["domain_whois"] = domain_whois_info

        domain_whois_history_info = DomainWhoIsHistoryParser()
        domain_whois_history_info.feed(self.html_content)
        domain_whois_history_info = domain_whois_history_info.domain_whois
        if domain_whois_history_info:
            bigdata_record["domain_whois_history"] = domain_whois_history_info

        host_records = ParserHelper.extract_hostname_data(self.html_content)
        if host_records:
            bigdata_record["host_records"] = host_records
        return bigdata_record
