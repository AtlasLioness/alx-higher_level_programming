#!/bin/bash
# displays size of body of response to reauest sent to URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
