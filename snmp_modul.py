#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
snmp_modul.py
Modul untuk monitoring SNMP ke perangkat.
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

from pysnmp.hlapi import (
    SnmpEngine, CommunityData, UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity, getCmd
)
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_snmp_vm = 1161
community = f"comm_{kode_cabang}"  # comm_047


def cek_snmp():
    """
    Ambil nilai sysName dari SNMP agent.
    OID: 1.3.6.1.2.1.1.5.0
    """
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host_vm, port_snmp_vm), timeout=15),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0"))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        
        if errorIndication:
            print(f"[SNMP] GAGAL: {str(errorIndication)}")
            return {"status": "gagal", "error": str(errorIndication)}
        elif errorStatus:
            print(f"[SNMP] GAGAL: {errorStatus.prettyPrint()}")
            return {"status": "gagal", "error": errorStatus.prettyPrint()}
        else:
            for vb in varBinds:
                sysname = str(vb[1])
                print(f"[SNMP] sysName: {sysname}")
                return {"status": "sukses", "sysname": sysname}
    except Exception as e:
        print(f"[SNMP] GAGAL: {str(e)}")
        return {"status": "gagal", "error": str(e)}


if __name__ == "__main__":
    cek_snmp()