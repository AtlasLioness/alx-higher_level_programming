#!/bin/bash
# sends DELETE to URL and displays body of response
curl -s "$1" -X DELETE
