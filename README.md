*Description*:
An application which enerates simulated PV (photovoltaic) power values (in kW). In the following picture of a real PV power output curve during a normal day

• Meter: This should produce messages to the broker with random but continuous values from 0 to 9000 Watts. This is to mock a regular home power consumption.
• PV simulator: listens to the broker for the meter values, generates a simulated PV power value and the last step is to add this value to the meter value and output the result.
• Writing  to a file: the result is saved in a file with timestamp (ts),  meter power value,  PV power value and the sum of the powers  (meter  + PV). The  period of a day (total_value)
with samples every couple of seconds (dt and ts). 

*Install*:
- offline: 
  pip install --no-index --find-links=wheelhouse -r requirements.txt
  - python setup.py develop
- online:
  - python setup.py develop

*Configure*:
- config file pvs.yaml allows to rewrite some variablies (such as rabbitmq host and port and report folder path)

*How to run*:
- run "simulator-consumer" -- in order to start the PV simulator which also consumes messages from meter (listener)
- run "meter-producer" -- in order to start meter which produces home power consumption (producer)
- run "tail -f report/{date}/report.txt" -- in order to read output

*Example of output*:
{"pv_value": 6677, "meter_value": 7420, "result_value": -743, "total_value": 41684960, "total_value_kw": 41684.96, "ts": 1609432213.120053, "dt": "2020-12-31 17:30:13.120053"}

*Tests*:
- pip install -r requirements_test.txt
- pytest tests
