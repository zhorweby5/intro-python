#!/usr/bin/env python

import requests

print("hello world")

print(requests.get("https://google.com/").text)

from cowsay import cowsay

print(cowsay('Hello World'))
