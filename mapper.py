#!/usr/bin/env python3
import sys

TARGET_CATEGORIES = {"Computers", "Cameras", "Video Games"}

for line_num, line in enumerate(sys.stdin, 1):
    parts = line.strip().split('\t')
    
    if len(parts) < 6:
        raise ValueError("Invalid input on line {}: Expected at least 6 fields, got {}".format(line_num, len(parts)))

    category = parts[3]
    amount = parts[4]

    if category not in TARGET_CATEGORIES:
        continue  # skip irrelevant categories

    try:
        float(amount)
        print("{}\t{}".format(category, amount))
    except ValueError:
        pass