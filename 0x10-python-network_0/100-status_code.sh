#!/bin/bash
# sends request to URL and displays only status code of response
curl -s -L -X HEAD -w "%{http_code}" "$1"
