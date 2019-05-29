openconfig parser
=================

.. raw:: html

    <table border=1>
      <col width="60%"><col width="20%"><col width="20%">      <tr>
        <th>path</th>
        <th>ios</th>
        <th>junos</th>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces</td>
        <td>&#x2705 <div style="font-family:'Lucida Console', monospace; font-size: 12px; line-height: 1">{'key': 'dev_conf', 'command': 'show running-config all'}</div>    </td>
        <td>&#x2705 <div style="font-family:'Lucida Console', monospace; font-size: 12px; line-height: 1">{'key': 'dev_conf', 'rpc': 'get-config'}</div>    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/name</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/name</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/type</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/loopback-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/description</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/enabled</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/config/openconfig-vlan:tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/loopback-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/ifindex</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/admin-status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/oper-status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/last-change</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/logical</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-unicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-broadcast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-multicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-discards</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-unknown-protos</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/in-fcs-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-unicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-broadcast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-multicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-discards</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/out-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/carrier-transitions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/counters/last-clear</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/state/openconfig-vlan:tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/config/up</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/config/down</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/state/up</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/hold-time/state/down</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/index</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config/index</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config/description</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/ifindex</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/admin-status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/oper-status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/last-change</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/logical</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-unicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-broadcast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-multicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-discards</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-unknown-protos</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/in-fcs-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-unicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-broadcast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-multicast-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-discards</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/out-errors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/carrier-transitions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/state/counters/last-clear</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/config/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/state/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged/config/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged/state/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-list</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-list/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-list/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/config/low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/config/high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/state/low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/single-tagged-range/state/high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/config/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/config/outer-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/state/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged/state/outer-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-list</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-list/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-list/config/outer-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-list/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-list/state/outer-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-list</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-list/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-list/config/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-list/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-list/state/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/config/inner-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/config/inner-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/state/inner-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-range/state/inner-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/config/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/config/outer-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/config/outer-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/state/inner-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/state/outer-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-outer-range/state/outer-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/config/inner-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/config/inner-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/config/outer-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/config/outer-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/state/inner-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/state/inner-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/state/outer-low-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/match/double-tagged-inner-outer-range/state/outer-high-vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/config/vlan-stack-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/config/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/config/tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/state/vlan-stack-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/state/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/ingress-mapping/state/tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/config/vlan-stack-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/config/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/config/tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/state/vlan-stack-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/state/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-vlan:vlan/egress-mapping/state/tpid</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/config/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/config/prefix-length</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state/prefix-length</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/state/origin</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/preempt</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/preempt-delay</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/accept-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/config/advertisement-interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/preempt</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/preempt-delay</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/accept-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/advertisement-interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/state/current-priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/interface-tracking</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/interface-tracking/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/interface-tracking/config/priority-decrement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/interface-tracking/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/addresses/address/vrrp/vrrp-group/interface-tracking/state/priority-decrement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/proxy-arp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/proxy-arp/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/proxy-arp/config/mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/proxy-arp/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/proxy-arp/state/mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/config/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/config/link-layer-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/state/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/state/link-layer-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/neighbors/neighbor/state/origin</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/unnumbered/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/config/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/config/dhcp-client</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/dhcp-client</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-error-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-forwarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-forwarded-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/in-discarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-error-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-forwarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-forwarded-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv4/state/counters/out-discarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/config/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/config/prefix-length</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state/prefix-length</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state/origin</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/state/status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/preempt</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/preempt-delay</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/accept-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/advertisement-interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/config/virtual-link-local</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/virtual-router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/preempt</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/preempt-delay</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/accept-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/advertisement-interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/current-priority</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/state/virtual-link-local</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/interface-tracking</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/interface-tracking/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/interface-tracking/config/priority-decrement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/interface-tracking/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/addresses/address/vrrp/vrrp-group/interface-tracking/state/priority-decrement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/config/interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/config/lifetime</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/config/suppress</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/state/interval</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/state/lifetime</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/router-advertisement/state/suppress</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/config/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/config/link-layer-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state/ip</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state/link-layer-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state/origin</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state/is-router</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/neighbors/neighbor/state/neighbor-state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/unnumbered/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/config/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/config/dup-addr-detect-transmits</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/config/dhcp-client</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/mtu</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/dup-addr-detect-transmits</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/dhcp-client</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-error-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-forwarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-forwarded-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/in-discarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-error-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-forwarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-forwarded-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-interfaces:interfaces/interface/subinterfaces/subinterface/openconfig-if-ip:ipv6/state/counters/out-discarded-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/state/counter-capability</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/config/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/config/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/state/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/config/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/config/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/state/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/state/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/state/matched-packets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/state/matched-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/input-interface/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/config/forwarding-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/config/log-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/state/forwarding-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/acl-sets/acl-set/acl-entries/acl-entry/actions/state/log-action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/config/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/state/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/config/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/config/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/state/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state/matched-packets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/ingress-acl-sets/ingress-acl-set/acl-entries/acl-entry/state/matched-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/config/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/config/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/state/set-name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry/state/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry/state/matched-packets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-acl:acl/interfaces/interface/egress-acl-sets/egress-acl-set/acl-entries/acl-entry/state/matched-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/config/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/config/set-tag</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/state/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/state/set-tag</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/config/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/config/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/config/metric</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/config/recurse</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/state/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/state/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/state/metric</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/state/recurse</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/static-routes/static/next-hops/next-hop/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/config/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/config/discard</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/config/set-tag</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/state/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/state/discard</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-local-routing:local-routes/local-aggregates/aggregate/state/set-tag</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/config/mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/state/mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/ip-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/masklength-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/config/ip-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/config/masklength-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/state/ip-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set/prefixes/prefix/state/masklength-range</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/neighbor-set/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/defined-sets/tag-sets/tag-set/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/config/call-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/config/install-protocol-eq</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/state/call-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/state/install-protocol-eq</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-interface/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/config/prefix-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/config/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/state/prefix-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-prefix-set/state/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/config/neighbor-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/config/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/state/neighbor-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-neighbor-set/state/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/config/tag-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/config/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/state/tag-set</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/conditions/match-tag-set/state/match-set-options</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/actions</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/actions/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/actions/config/policy-result</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/actions/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-routing-policy:routing-policy/policy-definitions/policy-definition/statements/statement/actions/state/policy-result</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances</td>
        <td>&#x2705 <div style="font-family:'Lucida Console', monospace; font-size: 12px; line-height: 1">{'key': 'dev_conf', 'command': 'show running-config all'}</div>    </td>
        <td>&#x2705 <div style="font-family:'Lucida Console', monospace; font-size: 12px; line-height: 1">{'key': 'dev_conf', 'rpc': 'get-config'}</div>    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/name</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/name</td>
        <td>&#x2705    </td>
        <td>&#x2705    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/config/route-distinguisher</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/description</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/router-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/state/route-distinguisher</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/config/encapsulation-type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/config/label-allocation-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/state/encapsulation-type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/encapsulation/state/label-allocation-mode</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/config/default-import-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/config/default-export-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/state/default-import-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/inter-instance-policies/apply-policy/state/default-export-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/src-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/dst-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/config/src-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/config/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/config/dst-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/config/default-import-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/state/src-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/state/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/state/dst-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/table-connections/table-connection/state/default-import-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/config/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/state/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/interfaces/interface/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/config/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/config/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/state/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/tables/table/state/address-family</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/connection-point-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/config/connection-point-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/state/connection-point-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/endpoint-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/endpoint-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/precedence</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/config/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/state/endpoint-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/state/precedence</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/state/type</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/state/active</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/local/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config/remote-system</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/config/virtual-circuit-identifier</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/state/remote-system</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/connection-points/connection-point/endpoints/endpoint/remote/state/virtual-circuit-identifier</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/config/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/config/status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/state/vlan-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/state/status</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/members</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/members/member</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/members/member/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/vlans/vlan/members/member/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/policy-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/config/policy-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/state/policy-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/config/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state/sequence-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state/matched-pkts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state/matched-octets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config/source-mac</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config/source-mac-mask</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config/destination-mac</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config/destination-mac-mask</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/config/ethertype</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state/source-mac</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state/source-mac-mask</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state/destination-mac</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state/destination-mac-mask</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/l2/state/ethertype</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config/source-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config/destination-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config/dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/config/hop-limit</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state/source-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state/destination-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state/dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv4/state/hop-limit</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/source-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/source-flow-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/destination-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/destination-flow-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/config/hop-limit</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/source-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/source-flow-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/destination-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/destination-flow-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/ipv6/state/hop-limit</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/config/source-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/config/destination-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/state/source-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/transport/state/destination-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config/discard</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config/decapsulate-gre</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config/network-instance</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config/path-selection-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/config/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state/discard</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state/decapsulate-gre</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state/network-instance</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state/path-selection-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/state/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/config/identifying-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/state/identifying-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/config/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/config/source</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/config/destination</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/config/ip-ttl</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/state/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/state/source</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/state/destination</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/action/encapsulate-gre/targets/target/state/ip-ttl</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/config/interface-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/config/apply-forwarding-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/state/interface-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/state/apply-forwarding-policy</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/interfaces/interface/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group/group-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group/config/group-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/policy-forwarding/path-selection-groups/path-selection-group/state/group-id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/config/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state/packets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state/octets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv4-unicast/ipv4-entry/state/decapsulate-header</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/config/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state/prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state/packets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state/octets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ipv6-unicast/ipv6-entry/state/decapsulate-header</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/ip-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/mpls-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/mpls-tc</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/ip-dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/ip-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/l4-src-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/config/l4-dst-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/ip-prefix</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/mpls-label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/mpls-tc</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/ip-dscp</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/ip-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/l4-src-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/l4-dst-port</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/packets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/octets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/policy-forwarding/policy-forwarding-entry/state/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/config/label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/state/label</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/state/packets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/state/octets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/mpls/label-entry/state/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/config/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/state/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/state/packets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/state/octets-forwarded</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/ethernet/mac-entry/state/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/config/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/state/id</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/state/color</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/state/backup-next-hop-group</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/config/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/state/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hop-groups/next-hop-group/next-hops/next-hop/state/weight</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/config/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state/index</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state/ip-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state/mac-address</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state/encapsulate-header</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/state/origin-protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/config/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/config/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/state/interface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/afts/next-hops/next-hop/interface-ref/state/subinterface</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/identifier</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/config</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/config/identifier</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/config/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/config/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/config/default-metric</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/state</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/state/identifier</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/state/name</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/state/enabled</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
      <tr>
        <td>/openconfig-network-instance:network-instances/network-instance/protocols/protocol/state/default-metric</td>
        <td>❌    </td>
        <td>❌    </td>
      </tr>
    </table>
