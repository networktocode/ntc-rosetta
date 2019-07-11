ntc-vrf
#######

A simplfied model to manage VRFs

Data nodes
==========
/vrf
----

Top container for VRF configuration and state

**nodetype**: ``container``


-----

/vrf/config
-----------

VRF configuration

**nodetype**: ``container``


-----

/vrf/config/vrfs
----------------

List of VRFs

**nodetype**: ``list``


-----

/vrf/config/vrfs/name
---------------------

Name of VRF

**nodetype**: ``leaf`` (list key)

**Type**: ``string``



-----

/vrf/state
----------

VRF state

**nodetype**: ``container``


-----

/vrf/state/vrfs
---------------

List of VRFs

**nodetype**: ``list``


-----

/vrf/state/vrfs/name
--------------------

Name of VRF

**nodetype**: ``leaf`` (list key)

**Type**: ``string``



-----



