from socketserver import ThreadingTCPServer, StreamRequestHandler

class Echo(StreamRequestHandler):
    def handle(self):
        peer = self.client_address
        print(f"[+] Conexão de {peer}")
        while True:
            data = self.rfile.readline()
            if not data:
                print(f"[-] Fim de conexão {peer}")
                break
            self.wfile.write(data)

if __name__ == "__main__":
    # 0.0.0.0 = escuta em todas as interfaces
    with ThreadingTCPServer(("0.0.0.0", 50001), Echo) as srv:
        print("Servidor TCP escutando em 0.0.0.0:50001")
        srv.serve_forever()

# sudo PYTHONPATH=$HOME/scapy python3 server.py