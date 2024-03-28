#!/usr/bin/python3
# Takes a URL, sends a request to the URL, and displays the value of the X-Request-Id variable in the response header

import urllib.request
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))

if __name__ == "__main__":
    main()
