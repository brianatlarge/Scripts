from pysnmp.hlapi import *

ips = [
"192.168.1.1",
"192.168.1.2"
]

for ip in ips:
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            UsmUserData('ReadOnly', authKey='authpass', privKey='privpass',
                authProtocol=usmHMACSHAAuthProtocol,
                privProtocol=usmAesCfb128Protocol),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if errorIndication:
        print("*Fail - " + ip)
    elif errorStatus:
        print("*Fail - " + ip)
    else:
        print("Pass - " + ip)
