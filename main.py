#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.py
Program utama integrasi semua modul.
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

from identitas import nim, nama, kode_cabang, buat_id_perangkat
from ssh_modul import cek_ssh
from snmp_modul import cek_snmp
from netconf_modul import cetak_pesan_netconf
from telemetry_modul import klasifikasi_telemetry


class LaporanCabang:
    """
    Class untuk merangkum laporan akhir dari semua modul.
    """
    def __init__(self):
        self.hasil_ssh = None
        self.hasil_snmp = None
        self.hasil_netconf = None
        self.hasil_telemetry = None
    
    def jalankan_semua(self):
        """
        Menjalankan semua modul secara berurutan.
        """
        print("=" * 60)
        print("LAPORAN AKHIR CABANG OTOMASI JARINGAN")
        print("=" * 60)
        
        # Bagian A: Identitas
        print("\n[IDENTITAS CABANG]")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Kode Cabang: {kode_cabang}")
        print(f"ID Perangkat: {buat_id_perangkat('router', '001')}")
        
        # Bagian B: SSH
        print("\n[MODUL SSH]")
        self.hasil_ssh = cek_ssh()
        
        # Bagian C: SNMP
        print("\n[MODUL SNMP]")
        self.hasil_snmp = cek_snmp()
        
        # Bagian D: NETCONF
        print("\n[MODUL NETCONF]")
        self.hasil_netconf = cetak_pesan_netconf()
        
        # Bagian E: Telemetry
        print("\n[MODUL TELEMETRY]")
        self.hasil_telemetry = klasifikasi_telemetry()
    
    def tampilkan_laporan(self):
        """
        Menampilkan ringkasan laporan akhir.
        """
        print("\n" + "=" * 60)
        print("RINGKASAN HASIL")
        print("=" * 60)
        
        if self.hasil_ssh and self.hasil_ssh["status"] == "sukses":
            print(f"✓ SSH: Berhasil (Host: {self.hasil_ssh['hostname']})")
        else:
            print("✗ SSH: Gagal")
        
        if self.hasil_snmp and self.hasil_snmp["status"] == "sukses":
            print(f"✓ SNMP: Berhasil (sysName: {self.hasil_snmp['sysname']})")
        else:
            print("✗ SNMP: Gagal")
        
        print("✓ NETCONF: Pesan dibuat")
        
        if self.hasil_telemetry:
            kritis_count = sum(1 for r in self.hasil_telemetry if r["status"] == "KRITIS")
            print(f"✓ Telemetry: {len(self.hasil_telemetry)} sampel dianalisis ({kritis_count} KRITIS)")
        
        print("=" * 60)


if __name__ == "__main__":
    laporan = LaporanCabang()
    laporan.jalankan_semua()
    laporan.tampilkan_laporan()