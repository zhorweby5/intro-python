#!/usr/bin/env python

import requests

print("hello world")

print(requests.get("https://google.com/").text)
