#!/usr/bin/env python3

import calendar
import sys

def display_calendar(year, month):
    try:
        cal = calendar.month(year, month)
        print(cal)
    except ValueError as e:
        print(f"Erreur: {e}")

def main():
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        for month in range(1, 13):
            display_calendar(year, month)
            print("\n" + "-" * 20 + "\n")
    elif len(sys.argv) == 3:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        display_calendar(year, month)
    else:
        print("Usage: calendar [mois] [année]")
        sys.exit(1)

if __name__ == "__main__":
    main()

