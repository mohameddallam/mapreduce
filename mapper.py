#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) >= 5:
        category = parts[3]
        amount = parts[4]
        try:
            float(amount)
            print("{}\t{}".format(category, amount))
        except ValueError:
            pass