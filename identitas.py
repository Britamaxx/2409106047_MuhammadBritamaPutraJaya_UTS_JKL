#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
identitas.py
Modul untuk identitas cabang dan informasi perangkat.
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

nim = "2409106047"
nama = "Muhammad Britama Putra Jaya"
kode_cabang = "047"


def buat_id_perangkat(jenis, nomor):
    """
    Membuat identitas unik untuk perangkat cabang.
    Format: <kode_cabang>-<jenis>-<nomor>
    """
    return f"{kode_cabang}-{jenis}-{nomor}"


if __name__ == "__main__":
    print(f"NIM: {nim}")
    print(f"Nama: {nama}")
    print(f"Kode Cabang: {kode_cabang}")
    print(f"ID Perangkat: {buat_id_perangkat('router', '001')}")