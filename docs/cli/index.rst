CLI
===

ntc_rosetta comes with a simple CLI tool to help with various things:

   1. Lint parsers/translators
   2. Print the supported models as an ASCII tree
   3. Print the parser/translator as an ASCII tree similar to the supported models output

To execute the command line tool type ``ntc_rosetta`` after installing the library::

   $ ntc_rosetta git:(docs) ✗ ntc_rosetta
   Usage: ntc_rosetta [OPTIONS] COMMAND [ARGS]...

   Options:
     --help  Show this message and exit.

   Commands:
     lint          Lint files/folders with Parsers/Translators: Errors/Warning...
     print-model   Prints the model as an ASCII tree
     print-parser  Prints a tree representation of a parser/translator.

The command line tool is self-documented and you can check it's documentation using the ``--help`` flag.

Lint
####
ntc_rosetta lint will lint the parsers and translators and offers several options to be specified::

   $ ntc_rosetta git:(docs) ✗ ntc_rosetta lint --help
   Usage: ntc_rosetta lint [OPTIONS] [FILEPATHS]...

     Lint files/folders with Parsers/Translators:

     Errors/Warning message codes:

       - E001: path is empty

       - E101: schema path couldn't be found

       - E102: schema path is invalid

       - W001: children is missing

       - W101: class attribute doesn't belong to the model

   Options:
     -i, --ignore TEXT             ignore error/warning codes - e.g. specify multiple -i to ignore more than one code

     -m, --model [openconfig|ntc]  model to lint - default: openconfig

     -j, --json / -t, --text       output format - default: text

     --help                        Show this message and exit.

It will define the FILEPATHS as the current working directory. If we're in the root of **ntc-rosetta** then we will need to either move to the **ntc_rosetta** folder or specify **ntc_rosetta** when executing the command::

    $ ntc_rosetta git:(docs) ✗ ntc_rosetta lint ntc_rosetta
    ntc_rosetta/parsers/ntc/ios/ntc_vlan/vlan.py:39:E101:Yangify.path couldn't be found in model: /ntc-vlan:vlan
    ntc_rosetta/parsers/ntc/ios/ntc_vlan/vlan.py:32:E101:Yangify.path couldn't be found in model: /ntc-vlan:vlan/config
    ntc_rosetta/parsers/ntc/ios/ntc_vlan/vlan.py:8:E101:Yangify.path couldn't be found in model: /ntc-vlan:vlan/config/vlans
    ntc_rosetta/parsers/ntc/ios/ntc_vlan/vlan.py:39:E101:Yangify.path couldn't be found in model: /ntc-vlan:vlan
    ntc_rosetta/parsers/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement config
    ntc_rosetta/parsers/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement state
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:91:W001:doesn't implement state
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:91:W001:doesn't implement hold-time
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:51:W001:doesn't implement tpid
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:28:W001:doesn't implement state
    ntc_rosetta/translators/ntc/ios/ntc_vlan/vlan.py:48:E101:Yangify.path couldn't be found in model: /ntc-vlan:vlan
    ntc_rosetta/translators/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement config
    ntc_rosetta/translators/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:101:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:101:W001:doesn't implement hold-time
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:67:W001:doesn't implement tpid
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement vlan
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement ipv4
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement ipv6
    <omitted for brevity>

As you can see it will lint both parsers and translators that live within the NTC Rosetta project. If we'd like to ignore errors, we can either specify a single -i CODE or several -i to ignore those errors and warnings::

    $ ntc_rosetta git:(docs) ✗ ntc_rosetta lint ntc_rosetta -i E101
    ntc_rosetta/parsers/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement config
    ntc_rosetta/parsers/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement state
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:91:W001:doesn't implement state
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:91:W001:doesn't implement hold-time
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:51:W001:doesn't implement tpid
    ntc_rosetta/parsers/openconfig/ios/openconfig_interfaces/interfaces.py:28:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement config
    ntc_rosetta/translators/openconfig/ios/openconfig_if_ethernet/ethernet.py:6:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:101:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:101:W001:doesn't implement hold-time
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:67:W001:doesn't implement tpid
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement state
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement vlan
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement ipv4
    ntc_rosetta/translators/openconfig/ios/openconfig_interfaces/interfaces.py:29:W001:doesn't implement ipv6

We only get W001 warnings now that we're ignoring the E101 errors. If we want to ignore both, we can execute the following command:
    $ ntc_rosetta git:(docs) ✗ ntc_rosetta lint ntc_rosetta -i E101 -i W001

Executing the command will provide us with no output as those are the only errors and warnings we're receiving.

Print Model
###########
ntc_rosetta print-model will print the available YANG structures available from the available vendor models within NTC Rosetta::

    $ ntc_rosetta git:(docs) ✗ ntc_rosetta print-model --help
    Usage: ntc_rosetta print-model [OPTIONS]

      Prints the model as an ASCII tree

    Options:
      -m, --model [openconfig|ntc]  model to lint - default: openconfig

      --help                        Show this message and exit.


Here is the output provided when specifying ntc as the model to print::

 $ ntc_rosetta git:(docs) ✗ ntc_rosetta print-model -m ntc
 +--rw ntc-arp:arp
 |  +--rw config
 |  |  +--rw entries* [ip-address]
 |  |  |  +--rw hw-address <mac-address(string)>
 |  |  |  +--rw ip-address <ip-address(union)>
 |  |  |  +--rw vrf <leafref>
 |  |  +--rw timeout? <uint16>
 |  +--ro state
 |     +--ro entries* [ip-address]
 |     |  +--ro hw-address <mac-address(string)>
 |     |  +--ro ip-address <ip-address(union)>
 |     |  +--ro vrf <leafref>
 |     +--ro timeout? <uint16>
 +--rw ntc-system:system
 |  +--rw config
 |  |  +--rw snmp
 |  |     +--rw communities* [name]
 |  |     |  +--rw access-list
 |  |     |  |  +--rw ipv4? <string>
 |  |     |  |  +--rw ipv6? <string>
 |  |     |  +--rw name <string>
 |  |     |  +--rw version? <snmp-version(enumeration)>
 |  |     +--rw contact? <string>
 |  |     +--rw description? <string>
 |  |     +--rw location? <string>
 |  |     +--rw name? <string>
 |  +--ro state
 |     +--ro snmp
 |        +--ro communities* [name]
 |        |  +--ro access-list
 |        |  |  +--ro ipv4? <string>
 |        |  |  +--ro ipv6? <string>
 |        |  +--ro name <string>
 |        |  +--ro version? <snmp-version(enumeration)>
 |        +--ro contact? <string>
 |        +--ro description? <string>
 |        +--ro location? <string>
 |        +--ro name? <string>
 +--rw ntc-vlan:vlan
 |  +--rw config
 |  |  +--rw vlans* [vlan-id]
 |  |     +--rw active? <boolean>
 |  |     +--rw name? <string>
 |  |     +--rw vlan-id <uint16>
 |  +--rw state
 |     +--rw vlans* [vlan-id]
 |        +--rw active? <boolean>
 |        +--rw members* <string>
 |        +--rw name? <string>
 |        +--rw vlan-id <uint16>
 +--rw ntc-vrf:vrf
    +--rw config
    |  +--rw vrfs* [name]
    |     +--rw name <string>
    +--rw state
       +--rw vrfs* [name]
          +--rw name <string>

Currently there is no way to filter a specific model within the available models such as ntc-vlan only within this CLI tool.

Print Parser
############
ntc_rosetta print-parser will print the tree representation of a parser/translator::

    $ ntc_rosetta git:(docs) ✗ ntc_rosetta print-parser --help
    Usage: ntc_rosetta print-parser [OPTIONS] DRIVER

      Prints a tree representation of a parser/translator.

      Parser/Translator needs to be properly linted for this to work

    Options:
      -j, --json / -t, --text       output format - default: text

      -m, --model [openconfig|ntc]  model to lint - default: openconfig

      --help                        Show this message and exit.


Here is the output provided when specifying ios as the driver::

 $ ntc_rosetta git:(docs) ✗ ntc_rosetta print-parser ios
 +--IOSParser
     +--openconfig-interfaces:interfaces (Interfaces)
     |   +--interface (Interface)
     |      +--config (InterfaceConfig)
     |      +--subinterfaces (Subinterfaces)
     |         +--subinterface (Subinterface)
     |            +--config (SubinterfaceConfig)
     +--openconfig-network-instance:network-instances (NetworkInstances)
        +--network-instance (NetworkInstance)
           +--config (NetowrkInstanceConfig)
           +--vlans (Vlans)
              +--vlan (Vlan)
                 +--config (VlanConfig)

If there were **ntc** parser data being returned, we could just see the specific parsers representation by specifying the model using the **-m** option followed by the model.
