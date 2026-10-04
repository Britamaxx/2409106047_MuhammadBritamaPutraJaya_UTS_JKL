#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
netconf_modul.py
Modul untuk membangun pesan NETCONF (edit-config).
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

import xml.etree.ElementTree as ET
from identitas import kode_cabang

vlan_id = kode_cabang  # 047


def buat_pesan_netconf():
    """
    Membangun pesan NETCONF <rpc><edit-config> untuk membuat VLAN.
    
    Layer breakdown:
    - Transport layer: RPC wrapper
    - Messages layer: <rpc>, <edit-config>
    - Operations layer: merge operation
    - Content layer: <config>, VLAN data
    """
    
    # Menggunakan ElementTree untuk membangun XML secara terstruktur
    rpc = ET.Element("rpc", {"message-id": "1"})
    
    # Messages layer: edit-config
    edit_config = ET.SubElement(rpc, "edit-config")
    target = ET.SubElement(edit_config, "target")
    ET.SubElement(target, "candidate")
    
    default_op = ET.SubElement(edit_config, "default-operation")
    default_op.text = "merge"
    
    # Operations layer + Content layer: VLAN configuration
    config = ET.SubElement(edit_config, "config")
    vlans = ET.SubElement(config, "vlans")
    
    vlan = ET.SubElement(vlans, "vlan")
    vlan_id_elem = ET.SubElement(vlan, "vlan-id")
    vlan_id_elem.text = vlan_id
    
    vlan_name = ET.SubElement(vlan, "name")
    vlan_name.text = f"VLAN_{vlan_id}"
    
    # Konversi ke string XML
    xml_str = ET.tostring(rpc, encoding='unicode')
    
    return xml_str


def cetak_pesan_netconf():
    """
    Mencetak pesan NETCONF yang dibangun.
    """
    pesan = buat_pesan_netconf()
    print("[NETCONF] Pesan edit-config yang dibangun:")
    print(pesan)
    return pesan


if __name__ == "__main__":
    cetak_pesan_netconf()