# Scapy and RobotFramework

## Minimal server requirements

File index.html only needs to exist.

```
server/
└── index.html
```

To serve file minimaly :
`$ python3 -m http.server 8000`

## scapy

```
sudo -E python3 test/robotframework/lib/sn.py
```

```
sudo -E python3 -m scapy
```

## robot

```
sudo -E python3 -m robot -d test/robotframework/output test/robotframework/rf.robot
```