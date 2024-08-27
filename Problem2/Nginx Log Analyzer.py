import re
from collections import Counter
from datetime import datetime

LOG_FILE = "/var/log/nginx/access.log"

def parse_log_line(line):
    """
    Parse a single line of the log file and return relevant data.
    This is based on the common log format.
    """
    regex = r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\S+)'
    match = re.match(regex, line)
    if match:
        return match.groupdict()
    return None

def analyze_log(log_file):
    status_counter = Counter()
    page_counter = Counter()
    ip_counter = Counter()
    total_requests = 0
    not_found_errors = 0

    with open(log_file, "r") as f:
        for line in f:
            log_data = parse_log_line(line)
            if log_data:
                total_requests += 1

                # Count status codes
                status_counter[log_data['status']] += 1

                # Count pages requested
                request_parts = log_data['request'].split()
                if len(request_parts) > 1:
                    page = request_parts[1]
                    page_counter[page] += 1

                # Count IP addresses
                ip_counter[log_data['ip']] += 1

                # Count 404 errors
                if log_data['status'] == '404':
                    not_found_errors += 1

    # Summarize report
    print(f"Total Requests: {total_requests}")
    print(f"404 Errors: {not_found_errors}")
    print("\nTop 10 Most Requested Pages:")
    for page, count in page_counter.most_common(10):
        print(f"{page}: {count} requests")

    print("\nTop 10 IP Addresses:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests")

    print("\nStatus Code Distribution:")
    for status, count in status_counter.items():
        print(f"{status}: {count} responses")

if __name__ == "__main__":
    analyze_log(LOG_FILE)