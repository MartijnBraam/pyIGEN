# pyIGEN

This is a python module for parsing the binary log messages from the IGEN Tech S-W02E solar panel monitor.
The code is tested with messages from a Solax TL 3600

## Usage

```python
>>> import igen
>>>
>>> # Get your data from somewhere. The size of a log message is 103 bytes
>>> my_data = socket.read(103)
>>>
>>> log = igen.parse(my_data)
>>> log
<IGENMessage 1222 watt (2.9 kWh today)>
>>> log.temperature
29.0
>>> # Get the output voltage, amps and power for each phase
>>> log.outputs()
[(235.7, 5.2, 1222), (0.0, 0.0, 0), (0.0, 0.0, 0)]
>>> # Get the input voltage and amps for each channel
>>> log.inputs()
[(337.7, 2.5), (253.1, 1.3), (0.0, 0.0)]
>>> # To get a quick overview of the datapoint use .report()
>>> log.report()
Logger: S36215A1080049
Temperature: 29.0 degree celcius

Inputs: 
  Channel 1:  337.70 V   2.50 A
  Channel 2:  253.10 V   1.30 A
  Channel 3:    0.00 V   0.00 A

Outputs: (49.98 Hz)
  L1:  235.70 V   5.20 A   1222 W
  L2:    0.00 V   0.00 A      0 W
  L3:    0.00 V   0.00 A      0 W

Energy today:        2.9 kWh
Energy overall:     10.8 kWh
Operational hours: 86
```

## monitor.py

The `monitor.py` file in this repo is a mini server that listens on UDP port 1337 and receives the log messages sent by
the S-W02E and displays the report for each message. Just use it with:

```bash
$ python3 monitor.py
```