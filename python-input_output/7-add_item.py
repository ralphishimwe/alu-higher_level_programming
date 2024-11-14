#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then saves them to a file"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    except Exception as e:
        print(f"An error occurred: {e}")
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
