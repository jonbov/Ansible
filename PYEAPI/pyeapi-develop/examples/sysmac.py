#!/usr/bin/env python
from __future__ import print_function
import pyeapi

pyeapi.load_config('nodes.conf')
node = pyeapi.connect_to('spine2.bovre.net')

output = node.enable('show version')

print(('My System MAC address is', output[0]['result']['systemMacAddress']))
