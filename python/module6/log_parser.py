from collections import Counter
from re import compile, match, search


class LogParser:
    """Apache2 access.log simple parser"""

    def __init__(self, log_name):
        self.log_name = log_name

    def get_most_common(self, amount: int):
        """Return specified amount of most frequently encountered addresses in a file"""
        ip_regex = compile(r"^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}")
        res = []
        with open(self.log_name, 'r') as log_file:
            for line in log_file:
                try:
                    ip = match(ip_regex, line)
                    res.append(ip[0])
                except TypeError:
                    pass
        return Counter(res).most_common(amount)

    def log_by_http_code(self, output_file, code: int):
        """Create output file and put lines with specified code to it"""
        status_code_regexp = compile(rf"\s{code}\s")
        with open(self.log_name, 'r') as log_file:
            with open(output_file, 'w') as output:
                for line in log_file:
                    if search(status_code_regexp, line):
                        output.write(line)
