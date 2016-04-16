import igen
import socketserver
import argparse
import requests

apikey = None
inverter_id = None


def solarview_submit(datapoint):
    json_body = {
        'key': apikey,
        'input': [
            {'volt': datapoint.pv1, 'amp': datapoint.pa1},
            {'volt': datapoint.pv2, 'amp': datapoint.pa2},
            {'volt': datapoint.pv3, 'amp': datapoint.pa3}
        ],
        'output': [
            {'power': datapoint.op1}
        ],
        'temperature': datapoint.temperature,
        'daily-total': datapoint.energy_today
    }
    url = 'http://solarview.org/api/push/inverter/{}'.format(inverter_id)
    requests.post(url, json=json_body)


class SolarServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(156)
        try:
            datapoint = igen.parse(data)
        except Exception:
            print("Invalid packet")
            return
        solarview_submit(datapoint)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IGEN to Influxdb proxy")
    parser.add_argument('--listen', '-l', type=int, help="listen port for IGEN module")
    parser.add_argument('--inverter', help="Inverter ID")
    parser.add_argument('--apikey', help="Inverter API Key", default="")
    args = parser.parse_args()

    apikey = args.apikey
    inverter_id = args.inverter

    print("Starting...")
    server = socketserver.TCPServer(('0.0.0.0', args.listen), SolarServer)
    print("Started")
    server.serve_forever()
