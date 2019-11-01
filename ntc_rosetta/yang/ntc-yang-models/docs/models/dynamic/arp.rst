ntc-arp
#######

Model to configure and retrieve operational state of ARP and ARP entries

Data nodes
==========
/arp
----

Top-level container for ARP model

**nodetype**: ``container``


-----

/arp/config
-----------

ARP configuration

**nodetype**: ``container``


-----

/arp/config/timeout
-------------------

Cache arp entries for this amount of time (seconds)

**nodetype**: ``leaf``

**Type**: ``uint16``



-----

/arp/config/entries
-------------------

List of ARP entries configured in the system

**nodetype**: ``list``


-----

/arp/config/entries/ip-address
------------------------------

IP address associated to the ARP entry

**nodetype**: ``leaf`` (list key)

**Type**: ``ntc-types:ip-address``



-----

/arp/config/entries/hw-address
------------------------------

Physical address associated to the ARP entry

**nodetype**: ``leaf``

**Type**: ``yang:mac-address``



-----

/arp/config/entries/vrf
-----------------------

VRF associoated to the ARP entry

**nodetype**: ``leaf``

**Type**: ``leafref``


* **path reference**: ``/vrf/config/vrfs/name``



-----

/arp/state
----------

ARP state

**nodetype**: ``container``


-----

/arp/state/timeout
------------------

Cache arp entries for this amount of time (seconds)

**nodetype**: ``leaf``

**Type**: ``uint16``



-----

/arp/state/entries
------------------

List of ARP entries in the system

**nodetype**: ``list``


-----

/arp/state/entries/ip-address
-----------------------------

IP address associated to the ARP entry

**nodetype**: ``leaf`` (list key)

**Type**: ``ntc-types:ip-address``



-----

/arp/state/entries/hw-address
-----------------------------

Physical address associated to the ARP entry

**nodetype**: ``leaf``

**Type**: ``yang:mac-address``



-----

/arp/state/entries/vrf
----------------------

VRF associoated to the ARP entry

**nodetype**: ``leaf``

**Type**: ``leafref``


* **path reference**: ``/vrf/state/vrfs/name``



-----



