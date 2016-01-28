from unittest import TestCase
import igen


class TestIGENMessage(TestCase):
    def test_datapoint_message(self):
        with open('fixtures/boot_point.bin', 'rb') as input_file:
            boot_message = input_file.read()
        self.assertEqual(len(boot_message), 103)
        parsed = igen.parse(boot_message)

        self.assertEqual(parsed.serial, "S36215A1080049")
        self.assertEqual(parsed.temperature, 15.0)

        self.assertEqual(parsed.pv1, 200.4)
        self.assertEqual(parsed.pv2, 199.8)
        self.assertEqual(parsed.pv3, 0)

        self.assertEqual(parsed.pa1, 0.0)
        self.assertEqual(parsed.pa2, 0.0)
        self.assertEqual(parsed.pa3, 0.0)

        self.assertEqual(parsed.ov1, 234.9)
        self.assertEqual(parsed.ov2, 0)
        self.assertEqual(parsed.ov3, 0)

        self.assertEqual(parsed.oa1, 0.1)
        self.assertEqual(parsed.oa2, 0)
        self.assertEqual(parsed.oa3, 0)

        self.assertEqual(parsed.oHz, 49.97)

        self.assertEqual(parsed.op1, 0)
        self.assertEqual(parsed.op2, 0)
        self.assertEqual(parsed.op3, 0)

        self.assertEqual(parsed.energy_today, 0)
        self.assertEqual(parsed.energy_overall, 7.9)
        self.assertEqual(parsed.operational_hours, 81)

        self.assertEqual(repr(parsed), "<IGENMessage 0 watt (0.0 kWh today)>")

    def test_datapoint_message2(self):
        with open('fixtures/normal_point.bin', 'rb') as input_file:
            boot_message = input_file.read()
        self.assertEqual(len(boot_message), 103)
        parsed = igen.parse(boot_message)

        self.assertEqual(parsed.serial, "S36215A1080049")
        self.assertEqual(parsed.temperature, 29.0)

        self.assertEqual(parsed.pv1, 337.7)
        self.assertEqual(parsed.pv2, 253.1)
        self.assertEqual(parsed.pv3, 0)

        self.assertEqual(parsed.pa1, 2.5)
        self.assertEqual(parsed.pa2, 1.3)
        self.assertEqual(parsed.pa3, 0.0)

        self.assertEqual(parsed.ov1, 235.7)
        self.assertEqual(parsed.ov2, 0)
        self.assertEqual(parsed.ov3, 0)

        self.assertEqual(parsed.oa1, 5.2)
        self.assertEqual(parsed.oa2, 0)
        self.assertEqual(parsed.oa3, 0)

        self.assertEqual(parsed.oHz, 49.98)

        self.assertEqual(parsed.op1, 1222)
        self.assertEqual(parsed.op2, 0)
        self.assertEqual(parsed.op3, 0)

        self.assertEqual(parsed.energy_today, 2.9)
        self.assertEqual(parsed.energy_overall, 10.8)
        self.assertEqual(parsed.operational_hours, 86)

        self.assertEqual(repr(parsed), "<IGENMessage 1222 watt (2.9 kWh today)>")