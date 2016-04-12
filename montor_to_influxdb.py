import igen
import socketserver
import argparse
from influxdb import InfluxDBClient

influxclient = None


def influx_submit(datapoint):
    json_body = [{
        'measurement': 'solar_inverter',
        'tags': {
            'system': datapoint.serial
        },
        'fields': {
            "input1_amp": datapoint.pa1,
            "input2_amp": datapoint.pa2,
            "input3_amp": datapoint.pa3,
            "input1_volt": datapoint.pv1,
            "input2_volt": datapoint.pv2,
            "input3_volt": datapoint.pv3,
            "output1_amp": datapoint.oa1,
            "output2_amp": datapoint.oa2,
            "output3_amp": datapoint.oa3,
            "output1_volt": datapoint.ov1,
            "output2_volt": datapoint.ov2,
            "output3_volt": datapoint.ov3,
            "output1_pwr": datapoint.op1,
            "output2_pwr": datapoint.op2,
            "output3_pwr": datapoint.op3,
            "temp": datapoint.temperature
        }
    }]
    influxclient.write_points(json_body)


class SolarServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(156)
        try:
            datapoint = igen.parse(data)
        except Exception:
            print("Invalid packet")
            return
        influx_submit(datapoint)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IGEN to Influxdb proxy")
    parser.add_argument('--listen', '-l', type=int, help="listen port for IGEN module")
    parser.add_argument('--database', help="Influx database name", default="solar")
    parser.add_argument('--username', help="Database username", default="root")
    parser.add_argument('--password', help="Database password", default="root")
    args = parser.parse_args()

    influxclient = InfluxDBClient('localhost', 8086, args.username, args.password, args.database)

    print("Starting...")
    server = socketserver.TCPServer(('0.0.0.0', args.listen), SolarServer)
    print("Started")
    server.serve_forever()
