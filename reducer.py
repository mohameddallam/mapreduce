#!/usr/bin/env python3
import sys

current_category = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    category, _ = line.split('\t', 1)

    if current_category == category:
        count += 1
    else:
        if current_category:
            print("{}\t{}".format(current_category, count))
        current_category = category
        count = 1

# Output the last one
if current_category:
    print("{}\t{}".format(current_category, count))