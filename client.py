import socket
import os
import sys

SERVER = '127.0.0.1'
PORT = 1111

def send_file(mode, filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER, PORT))
        s.send(mode.ljust(10).encode())  # mode fixed 10 bytes
        s.send(str(len(data)).zfill(16).encode())
        s.send(data)

        # Terima hasil
        size = int(s.recv(16).decode())
        result = s.recv(size)

        # Simpan file
        if mode == 'encode':
            outname = filepath + '.b64'
        elif mode == 'decode':
            outname = filepath.replace('.b64', '') + '.decoded'
        else:
            outname = 'output.data'

        with open(outname, 'wb') as f:
            f.write(result)

        print(f"[SUCCESS] Hasil disimpan di: {outname}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("❗ Usage: python client.py encode|decode file")
        sys.exit(1)

    mode = sys.argv[1]
    filepath = sys.argv[2]
    send_file(mode, filepath)
