#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL, and displays the
body of the response. If the HTTP status code is greater than or equal to 400,
it prints an error message with the HTTP status code.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)

        print(response.text)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
