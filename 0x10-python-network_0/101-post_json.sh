#!/bin/bash
# sends JSON POST request to URL and displays body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
