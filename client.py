import socket

HOST = '127.0.0.1'  # Alamat IP server
PORT = 5055         # Nomor port server

def send_request(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Lakukan koneksi ke server

        # Kirim permintaan HTTP untuk file tertentu
        request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filename, HOST)
        s.sendall(request.encode())

        # Terima dan simpan respons dari server
        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

    return response.decode()

# Contoh penggunaan: meminta file index.html dari server
filename = "coba.txt"
server_response = send_request(filename)
print("Response from server for", filename + ":")
print(server_response)
