import json
import re


class DnsHistoryParser:

    def __init__(self, html_content):
        self.__html = html_content

    @staticmethod
    def __ext_table_data__(web_content):
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

    @property
    def report(self):
        extracted_html_tables, max_len = self.__ext_table_data__(self.__html)
        history_data = []
        if len(extracted_html_tables) > 0:
            timeline_table = extracted_html_tables[0]
            if isinstance(timeline_table, list):
                if "<th scope=\"col\">Old Hoster</th>".lower() in str(timeline_table).lower():
                    for history_record in timeline_table[1:]:
                        extract_row_record = []
                        for record_column in history_record:
                            transaction_value = re.findall(r'>(.+?)<', record_column)
                            if len(transaction_value) == 1:
                                transaction_value = str(transaction_value[0]).replace("<center>", "")
                                transaction_value = str(transaction_value).replace("&nbsp;", " ")
                                if 'N/A' in transaction_value:
                                    transaction_value = "N/A"
                                elif transaction_value.lower() == "transfer":
                                    transaction_value = "Transfer"
                                elif transaction_value.lower() == "added":
                                    transaction_value = "Added"
                                elif transaction_value.lower() == "new":
                                    transaction_value = "New"
                                elif transaction_value.lower() == "removed":
                                    transaction_value = "Removed"
                                elif transaction_value.lower() == "deleted":
                                    transaction_value = "Deleted"
                                elif transaction_value.lower() == "epoch":
                                    transaction_value = "Epoch"
                                extract_row_record.append(
                                    transaction_value
                                )
                            else:
                                extract_row_record.append(
                                    ""
                                )
                        if extract_row_record:
                            host_record = {
                                "old_web_host": str(extract_row_record[0]).lower().rstrip().strip(),
                                "new_web_host": str(extract_row_record[1]).lower().rstrip().strip(),
                                "month_year": str(extract_row_record[2]).lower().rstrip().strip(),
                                "zone_date": str(extract_row_record[3]).lower().rstrip().strip(),
                                "transaction": str(extract_row_record[4]).lower().rstrip().strip(),

                            }
                            history_data.append(host_record)

        return json.dumps(history_data)
