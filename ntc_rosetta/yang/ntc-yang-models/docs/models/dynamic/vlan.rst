ntc-vlan
########

Model to configure and retrieve operational state of VLANs

Data nodes
==========
/vlan
-----

Top-level container for VLAN configuration and state

**nodetype**: ``container``


-----

/vlan/config
------------

Top-level container for VLAN configuration

**nodetype**: ``container``


-----

/vlan/config/vlans
------------------

List of VLANs

**nodetype**: ``list``


-----

/vlan/config/vlans/vlan-id
--------------------------

VLAN identifier

**nodetype**: ``leaf`` (list key)

**Type**: ``uint16``


* **range**: ``1..4094``



-----

/vlan/config/vlans/name
-----------------------

VLAN name

**nodetype**: ``leaf``

**Type**: ``string``



-----

/vlan/config/vlans/active
-------------------------

Whether the VLAN is enabled and bridging traffic or not

**nodetype**: ``leaf``

**Type**: ``boolean``



-----

/vlan/state
-----------

Top-level container for VLAN state

**nodetype**: ``container``


-----

/vlan/state/vlans
-----------------

List of VLANs

**nodetype**: ``list``


-----

/vlan/state/vlans/vlan-id
-------------------------

VLAN identifier

**nodetype**: ``leaf`` (list key)

**Type**: ``uint16``


* **range**: ``1..4094``



-----

/vlan/state/vlans/name
----------------------

VLAN name

**nodetype**: ``leaf``

**Type**: ``string``



-----

/vlan/state/vlans/active
------------------------

Whether the VLAN is enabled and bridging traffic or not

**nodetype**: ``leaf``

**Type**: ``boolean``



-----

/vlan/state/vlans/members
-------------------------

Interfaces in this VLAN

**nodetype**: ``leaf-list``

**Type**: ``string``



-----



