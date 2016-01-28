import struct


def parse(message):
    return IGENMessage.from_bytes(message)


class IGENMessage(object):
    def __init__(self):
        self.serial = None
        self.temperature = None
        self.pv1 = 0
        self.pv2 = 0
        self.pv3 = 0
        self.pa1 = 0
        self.pa2 = 0
        self.pa3 = 0
        self.ov1 = 0
        self.ov2 = 0
        self.ov3 = 0
        self.oa1 = 0
        self.oa2 = 0
        self.oa3 = 0
        self.oHz = 0
        self.op1 = 0
        self.op2 = 0
        self.op3 = 0
        self.energy_today = None
        self.energy_overall = None
        self.operational_hours = None

    @classmethod
    def from_bytes(cls, data):
        if len(data) != 103:
            raise Exception('Packet should be exactly 103 bytes')

        self = cls()

        parsed = struct.unpack('!17x 14s H HHH HHH HHH HHH H HHH 4x H 2x H 2x H 24x', data)
        self.serial = parsed[0].decode('ascii')

        self.temperature = parsed[1] / 10

        self.pv1 = parsed[2] / 10
        self.pv2 = parsed[3] / 10
        self.pv3 = parsed[4] / 10

        self.pa1 = parsed[5] / 10
        self.pa2 = parsed[6] / 10
        self.pa3 = parsed[7] / 10

        self.oa1 = parsed[8] / 10
        self.oa2 = parsed[9] / 10
        self.oa3 = parsed[10] / 10

        self.ov1 = parsed[11] / 10
        self.ov2 = parsed[12] / 10
        self.ov3 = parsed[13] / 10

        self.oHz = parsed[14] / 100

        self.op1 = parsed[15]
        self.op2 = parsed[16]
        self.op3 = parsed[17]

        self.energy_today = parsed[18] / 100
        self.energy_overall = parsed[19] / 10

        self.operational_hours = parsed[20]

        return self

    def output(self):
        return [
            (self.ov1, self.oa1, self.op1),
            (self.ov2, self.oa2, self.op2),
            (self.ov3, self.oa3, self.op3)
        ]

    def __repr__(self):
        total_power = self.op1 + self.op2 + self.op3
        return "<IGENMessage {} watt ({} kWh today)>".format(total_power, self.energy_today)
