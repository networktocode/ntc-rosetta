# ntc_rosetta

ntc_rosetta leverages [yangify](https://github.com/networktocode/yangify) to implement a set of "drivers" that can:

1. Transform network devices' native configuration/state into structured data that conform to YANG models
2. Transform data structures that conform to YANG models into network device's native configuration/data structures
3. Merge configurations

## Parsing

    >>> from ntc_rosetta import get_driver
    >>>
    >>> ios = get_driver("ios", "openconfig")
    >>> ios_driver = ios()
    >>> with open("data/ios/config.txt", "r") as f:
    >>>     config = f.read()
    >>> print(config)
    interface FastEthernet1
       description This is Fa1
       shutdown
       exit
    !
    vlan 10
       name prod
       no shutdown
       exit
    !
    vlan 20
       name dev
       shutdown
       exit
    !
    >>> parsed = ios_driver.parse(native={"dev_conf": config})
    >>> import json
    >>> print(json.dumps(parsed.raw_value(), indent=4))
    {
        "openconfig-interfaces:interfaces": {
            "interface": [
                {
                    "name": "FastEthernet1",
                    "config": {
                        "name": "FastEthernet1",
                        "type": "iana-if-type:ethernetCsmacd",
                        "description": "This is Fa1",
                        "enabled": false
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": 1,
                                "config": {
                                    "index": 1,
                                    "description": "This is Fa1.1"
                                }
                            },
                            {
                                "index": 2,
                                "config": {
                                    "index": 2,
                                    "description": "This is Fa1.2"
                                }
                            }
                        ]
                    }
                },
            ]
        },
        "openconfig-network-instance:network-instances": {
            "network-instance": [
                {
                    "name": "default",
                    "config": {
                        "name": "default"
                    },
                    "vlans": {
                        "vlan": [
                            {
                                "vlan-id": 10,
                                "config": {
                                    "vlan-id": 10,
                                    "name": "prod",
                                    "status": "ACTIVE"
                                }
                            },
                            {
                                "vlan-id": 20,
                                "config": {
                                    "vlan-id": 20,
                                    "name": "dev",
                                    "status": "SUSPENDED"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

## Translating

    >>> from ntc_rosetta import get_driver
    >>> 
    >>> ios = get_driver("ios", "openconfig")
    >>> ios_processor = ios()
    >>> data = {
    >>>     "openconfig-interfaces:interfaces": {
    >>>         "interface": [
    >>>             {
    >>>                 "name": "FastEthernet1",
    >>>                 "config": {
    >>>                     "name": "FastEthernet1",
    >>>                     "type": "iana-if-type:ethernetCsmacd",
    >>>                     "description": "This is Fa1",
    >>>                     "enabled": False
    >>>                 },
    >>>                 "subinterfaces": {
    >>>                     "subinterface": [
    >>>                         {
    >>>                             "index": 1,
    >>>                             "config": {
    >>>                                 "index": 1,
    >>>                                 "description": "This is Fa1.1"
    >>>                             }
    >>>                         },
    >>>                         {
    >>>                             "index": 2,
    >>>                             "config": {
    >>>                                 "index": 2,
    >>>                                 "description": "This is Fa1.2"
    >>>                             }
    >>>                         }
    >>>                     ]
    >>>                 }
    >>>             },
    >>>         ]
    >>>     },
    >>>     "openconfig-network-instance:network-instances": {
    >>>         "network-instance": [
    >>>             {
    >>>                 "name": "default",
    >>>                 "config": {
    >>>                     "name": "default"
    >>>                 },
    >>>                 "vlans": {
    >>>                     "vlan": [
    >>>                         {
    >>>                             "vlan-id": 10,
    >>>                             "config": {
    >>>                                 "vlan-id": 10,
    >>>                                 "name": "prod",
    >>>                                 "status": "ACTIVE"
    >>>                             }
    >>>                         },
    >>>                         {
    >>>                             "vlan-id": 20,
    >>>                             "config": {
    >>>                                 "vlan-id": 20,
    >>>                                 "name": "dev",
    >>>                                 "status": "SUSPENDED"
    >>>                             }
    >>>                         }
    >>>                     ]
    >>>                 }
    >>>             }
    >>>         ]
    >>>     }
    >>> }
    >>> native = ios_processor.translate(candidate=data)
    >>> print(native)
    interface FastEthernet1
       description This is Fa1
       shutdown
       exit
    !
    interface FastEthernet1.1
       description This is Fa1.1
       exit
    !
    interface FastEthernet1.2
       description This is Fa1.2
       exit
    !
    interface FastEthernet3
       description This is Fa3
       no shutdown
       switchport mode access
       switchport access vlan 10
       exit
    !
    interface FastEthernet4
       shutdown
       switchport mode trunk
       switchport trunk allowed vlan 10,20
       exit
    !
    vlan 10
       name prod
       no shutdown
       exit
    !
    vlan 20
       name dev
       shutdown
       exit
    !
