ntc-system
##########

Model to configure and retrieve system data

Types
=====
snmp-version
------------

SNMP version


**type**: ``enumeration``


* ``SNMP_VERESION_1``: SNMP version 1


* ``SNMP_VERSION_2C``: SNMP version 2c


* ``SNMP_VERSION_3``: SNMP version 3

Data nodes
==========
/system
-------

Top level container for system configuration and state

**nodetype**: ``container``


-----

/system/config
--------------

Top level container for system configuration

**nodetype**: ``container``


-----

/system/config/snmp
-------------------

Top level container for SNMP configuration

**nodetype**: ``container``


-----

/system/config/snmp/communities
-------------------------------

List of communities in the system

**nodetype**: ``list``


-----

/system/config/snmp/communities/name
------------------------------------

Name of community

**nodetype**: ``leaf`` (list key)

**Type**: ``string``



-----

/system/config/snmp/communities/version
---------------------------------------

SNMP version allowed by the community

**nodetype**: ``leaf``

**Type**: ``snmp-version``



-----

/system/config/snmp/communities/access-list
-------------------------------------------

Access list protecting the community

**nodetype**: ``container``


-----

/system/config/snmp/communities/access-list/ipv4
------------------------------------------------

IPv4 access-list

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/config/snmp/communities/access-list/ipv6
------------------------------------------------

IPv6 access-list

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/config/snmp/name
------------------------

Name of the commnity

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/config/snmp/description
-------------------------------

Description of the system

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/config/snmp/contact
---------------------------

Contact information for the system

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/config/snmp/location
----------------------------

Location information of the system

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state
-------------

Top level container for system state

**nodetype**: ``container``


-----

/system/state/snmp
------------------

Top level container for SNMP state

**nodetype**: ``container``


-----

/system/state/snmp/communities
------------------------------

List of communities in the system

**nodetype**: ``list``


-----

/system/state/snmp/communities/name
-----------------------------------

Name of community

**nodetype**: ``leaf`` (list key)

**Type**: ``string``



-----

/system/state/snmp/communities/version
--------------------------------------

SNMP version allowed by the community

**nodetype**: ``leaf``

**Type**: ``snmp-version``



-----

/system/state/snmp/communities/access-list
------------------------------------------

Access list protecting the community

**nodetype**: ``container``


-----

/system/state/snmp/communities/access-list/ipv4
-----------------------------------------------

IPv4 access-list

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state/snmp/communities/access-list/ipv6
-----------------------------------------------

IPv6 access-list

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state/snmp/name
-----------------------

Name of the commnity

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state/snmp/description
------------------------------

Description of the system

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state/snmp/contact
--------------------------

Contact information for the system

**nodetype**: ``leaf``

**Type**: ``string``



-----

/system/state/snmp/location
---------------------------

Location information of the system

**nodetype**: ``leaf``

**Type**: ``string``



-----



