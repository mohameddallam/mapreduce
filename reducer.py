#!/usr/bin/env python3
import sys

current_category = None
total = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        category, amount = line.split('\t', 1)
        amount = float(amount)
    except ValueError:
        continue

    if current_category == category:
        total += amount
        count += 1
    else:
        if current_category:
            avg = total / count
            print("{}\t{:.2f}".format(current_category, avg))
        current_category = category
        total = amount
        count = 1

# Output last category
if current_category and count > 0:
    avg = total / count
    print("{}\t{:.2f}".format(current_category, avg))