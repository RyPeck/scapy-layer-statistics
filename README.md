scapy-layer-statistics
======================

Retrieves statistics from the installed scapy module about the layers implemented. Right now it retrieves information about naming conventions on specific layers. Goal is to create something that is able to go through previous versions of scapy and learn collect data about the number of fields, layers, etc.

ToDo
-------
* Create Pages for statistics
* Put everything in a class (possibly)
* Download from scapy repository old releases and generate graph overtime of statistics
* Pull more information about layers
* Distinguish between true layers and layers that don't "stand alone", e.g. IP and IPOption
