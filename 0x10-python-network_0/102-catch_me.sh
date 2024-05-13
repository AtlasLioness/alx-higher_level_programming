#!/bin/bash
#/ makes request to 0.0.0.0:5000/catch_me to cause response You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "You got me!"
