# pyIGEN

This is a python module for parsing the binary log messages from the IGEN solar panel monitor.

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
>>> log.output()
[(235.7, 5.2, 1222), (0.0, 0.0, 0), (0.0, 0.0, 0)]
```