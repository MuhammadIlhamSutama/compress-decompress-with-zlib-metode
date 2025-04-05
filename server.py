import socket
import zlib
import base64

HOST = '0.0.0.0'
PORT = 9999

def handle_client(conn):
    # Terima mode (encode/decode)
    mode = conn.recv(10).decode().strip()
    print(f"[MODE] {mode}")

    # Terima ukuran data
    size = int(conn.recv(16).decode().strip())
    data = conn.recv(size)

    if mode == 'encode':
        compressed = zlib.compress(data)
        encoded = base64.b64encode(compressed)
        result = encoded
    elif mode == 'decode':
        try:
            compressed = base64.b64decode(data)
            result = zlib.decompress(compressed)
        except Exception as e:
            result = f"ERROR: {str(e)}".encode()
    else:
        result = b"ERROR: Invalid mode"

    # Kirim balik hasil
    conn.send(str(len(result)).zfill(16).encode())
    conn.send(result)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVER READY] Listening on port {PORT}")
        while True:
            conn, addr = s.accept()
            print(f"[CONNECTED] {addr}")
            handle_client(conn)

if __name__ == '__main__':
    main()
