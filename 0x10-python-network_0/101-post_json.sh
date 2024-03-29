#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file and displays the body of the response
json_file="$2"
response=$(curl -s "$1" -X POST -H "Content-Type: application/json" --data-binary "@$json_file")
if [[ $response == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
