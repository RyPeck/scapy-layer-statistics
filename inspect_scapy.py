#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import scapy.layers.all
from collections import Counter

all_scapy_layers = inspect.getmembers(scapy.layers.all)

from scapy.packet import Packet

packet_subclasses = []

for item in all_scapy_layers:
    if inspect.isclass(item[1]):
        if issubclass(item[1], Packet):
            packet_subclasses.append(item[1])

all_fields = reduce(lambda x, y: x + y,
                    [pkt_cls.fields_desc for pkt_cls in packet_subclasses])

print "Number of fields in scapy", len(all_fields)

field_count = Counter(all_fields)

print "Top 10 most common field names"
for n, item in enumerate(field_count.most_common(10)):
    print (n+1), item[0].name, item[1]

print ("="*79)

all_fields_fmts = [field.fmt for field in all_fields]

field_fmts_count = Counter(all_fields_fmts)

print "Most common field.fmts names"
for n, item in enumerate(field_fmts_count.most_common()):
    print (n+1), item[0], item[1]
