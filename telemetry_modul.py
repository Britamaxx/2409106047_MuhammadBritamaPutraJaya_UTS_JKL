#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
telemetry_modul.py
Modul untuk analisis data telemetry CPU usage.
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

# Data sampel CPU Usage (in-util) diturunkan dari digit NIM
# NIM: 2409106047
# Sampel 1: 24 (digit 1+2), Sampel 2: 91 (digit 5+4), Sampel 3: 47 (digit 9+10)
data_telemetry = {
    "sampel_1": {"timestamp": "2026-10-04T10:00:00", "cpu_usage": 24},
    "sampel_2": {"timestamp": "2026-10-04T10:05:00", "cpu_usage": 91},
    "sampel_3": {"timestamp": "2026-10-04T10:10:00", "cpu_usage": 47},
}


def klasifikasi_telemetry():
    """
    Mengklasifikasikan CPU usage ke kategori:
    - KRITIS: > 80
    - WASPADA: 50-80
    - NORMAL: < 50
    """
    hasil = []
    
    for key, data in data_telemetry.items():
        cpu = data["cpu_usage"]
        
        if cpu > 80:
            status = "KRITIS"
        elif 50 <= cpu <= 80:
            status = "WASPADA"
        else:
            status = "NORMAL"
        
        hasil.append({
            "sampel": key,
            "cpu_usage": cpu,
            "status": status
        })
        print(f"[TELEMETRY] {key}: CPU {cpu}% → {status}")
    
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()