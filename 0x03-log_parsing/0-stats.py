#!/usr/bin/python3
'''creating a log parsing method.'''
import sys
import re

pattern = r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

# Initialize variables to store metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            # Extract status code and file size
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update total file size and status code counts
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f'{code}: {count}')

except KeyboardInterrupt:
    # Handle Ctrl+C by printing the statistics
    print(f'Total file size: {total_size}')
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f'{code}: {count}')
