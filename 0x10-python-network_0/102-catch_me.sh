#!/bin/bash
#/ makes request to 0.0.0.0:5000/catch_me to cause response You got me!
curl -sX PUT "0.0.0.0:5000/catch_me" -d "You got me!"
