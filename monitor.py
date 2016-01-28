import igen
import socketserver


class SolarServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(156)
        try:
            datapoint = igen.parse(data)
        except Exception:
            print("Invalid packet")
        datapoint.report()
        print("--------------------")


if __name__ == "__main__":
    print("Starting...")
    server = socketserver.TCPServer(('0.0.0.0', 1337), SolarServer)
    print("Started")
    server.serve_forever()