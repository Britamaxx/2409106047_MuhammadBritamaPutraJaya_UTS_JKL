#Muhammad Britama Putra Jaya | 2409106047
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ssh_modul.py
Modul untuk akses SSH ke VM/perangkat jarak jauh.
Pembuat: Muhammad Britama Putra Jaya (2409106047)
"""

import paramiko
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_ssh_vm = 2222
user_ssh = f"admin_{kode_cabang}"  # admin_047
pass_ssh = "123"  # Sesuaikan dengan password VM kamu


def cek_ssh():
    """
    Login ke VM via SSH dan jalankan perintah diagnostik.
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh,
                       password=pass_ssh, timeout=5)
        
        # Perintah 1: hostname
        stdin, stdout, stderr = client.exec_command("hostname")
        hasil_hostname = stdout.read().decode().strip()
        
        # Perintah 2: whoami
        stdin, stdout, stderr = client.exec_command("whoami")
        hasil_whoami = stdout.read().decode().strip()
        
        print("[SSH] Koneksi berhasil")
        print(f"[SSH] Hostname: {hasil_hostname}")
        print(f"[SSH] User: {hasil_whoami}")
        
        client.close()
        return {"status": "sukses", "hostname": hasil_hostname, "user": hasil_whoami}
    except Exception as e:
        print(f"[SSH] GAGAL: {str(e)}")
        return {"status": "gagal", "error": str(e)}


if __name__ == "__main__":
    cek_ssh()