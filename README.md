# UTS Jaringan Komputer Lanjut - Integrasi Network dengan Python

**NIM:** 2409106047  
**Nama:** Muhammad Britama Putra Jaya  
**Kode Cabang:** 047  
**Deadline:** 4 Oktober 2026, 23:59 WITA

## Deskripsi Project

Project ini mengintegrasikan lima komponen jaringan menggunakan Python:
1. **Identitas Cabang** - Informasi dan identifikasi perangkat
2. **SSH/Paramiko** - Akses jarak jauh ke VM
3. **SNMP/PySNMP** - Monitoring sistem
4. **NETCONF** - Konfigurasi terstruktur (XML)
5. **Telemetry** - Analisis data real-time

## Struktur Folder
2409106047_MuhammadBritamaPutraJaya_UTS_JKL/
├── .gitignore
├── README.md
├── main.py
├── identitas.py
├── ssh_modul.py
├── snmp_modul.py
├── netconf_modul.py
└── telemetry_modul.py

## Cara Menjalankan

### 1. Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies
```bash
pip install paramiko pysnmp==4.4.12 pyasn1==0.4.8 pyasyncore
```

### 3. Jalankan Program
```bash
python main.py
```

## Personalisasi yang Digunakan

- **Kode Cabang:** 047 (3 digit terakhir NIM)
- **Username SSH:** admin_047
- **Community String SNMP:** comm_047
- **VLAN ID:** 047
- **Data Telemetry:** Diturunkan dari digit NIM (24, 91, 47)

## Fitur Utama

✓ Integrasi SSH dengan error handling  
✓ Monitoring SNMP dengan SNMPv2c  
✓ Pembuatan pesan NETCONF XML  
✓ Klasifikasi data telemetry CPU usage  
✓ Laporan akhir gabungan dalam satu program  
✓ Version control dengan Git dan commit terstruktur

## Catatan

- Credential SSH dan SNMP sudah dikonfigurasi sesuai lingkungan lokal
- NETCONF dijalankan tanpa perangkat fisik (fokus struktur XML)
- Data telemetry adalah sampel yang sudah di-decode