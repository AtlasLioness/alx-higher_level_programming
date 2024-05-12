#!/bin/bash
# sends request to URL and displays only status code of response
curl -sLw "%{http_code}" -o /dev/null "$1"
