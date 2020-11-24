#! python3
# prints the weather for a location in the cmdline

import json, requests, sys

# Compute location from cmdline args
if len(sys.argv) < 2:
  print('Usage: quickWeather.py location')
  sys.exit()
location = ' '.join(sys.argv[1:])

# TODO Download the JSON data from OpenWeatherMap.org's API.

# TODO Load JSON data into a Python variable.