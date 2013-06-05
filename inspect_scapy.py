#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import scapy.layers.all
from collections import Counter

all_scapy_layers = inspect.getmembers(scapy.layers.all)

from scapy.packet import Packet

import scapy.config

from operator import itemgetter

scapy_version = scapy.config.Conf.version

print "Scapy Version", scapy_version

packet_subclasses = []
field_layer_dict = {}

for item in all_scapy_layers:
    if inspect.isclass(item[1]):
        if issubclass(item[1], Packet):
            packet_subclasses.append(item[1])

# Add all the fields into one big list
all_fields = reduce(lambda x, y: x + y,
                    [pkt_cls.fields_desc for pkt_cls in packet_subclasses])

# Dictionary structure so when we have a specific field, we can see what layer
# it came from
for pkt_cls in packet_subclasses:
    for fld in pkt_cls.fields_desc:
        if fld not in field_layer_dict:
            field_layer_dict[fld] = [pkt_cls]
        else:
            field_layer_dict[fld].append(pkt_cls)


def getFieldCount(all_fields):
    """Count the occurence of each field name, return dictionary with tally"""

    # This has repeats of the names for some reason
    field_count = Counter(all_fields)

    return field_count


def printNTopFieldNames(field_count, num=None):
    """Print <num> of top field names. None prints all info"""

    flds = {}

    for n, item in enumerate(field_count.most_common(num)):
        if item[1] not in flds:
            flds[item[1]] = [[item[0].name, item]]
        else:
            flds[item[1]].append([item[0].name, item])

    for key in sorted(flds.keys(), reverse=True):
        s = sorted(flds[key], key=itemgetter(0))
        for i in s:
            print key, i[0], i[1]


def getFieldFmtsCount(all_fields):
    """Count the occurence of different fmts for all of the fields"""

    all_fields_fmts = [field.fmt for field in all_fields]

    field_fmts_count = Counter(all_fields_fmts)


def printFieldFmtsCounts(fields_fmts_count):
    """Print the count information of field formats"""

    for n, item in enumerate(field_fmts_count.most_common()):
        print (n + 1), item[0], item[1]


def findFieldName(all_fields, name):
    """Find the occurances of a field with a certain name"""

    for fld in all_fields:
        if fld.name == name:
            print fld.name

print "Number of fields in scapy", len(all_fields)
print "Number of unique scapy fields", len(field_layer_dict)

field_count = getFieldCount(all_fields)

#printNTopFieldNames(field_count)
