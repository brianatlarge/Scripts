# Scripts
Useful scripts I wrote

## snmp_scan.py
This takes an array of IP addresses and checks if it can connect over SNMPv3 using supplied credentials. This can be used to ensure ACL's are updated correctly on end devices.

## update_snmpacl.py
This will log into a list of IP's via SSH using the supplied credentials and update an ACL to permit access. This is for Cisco IOS devices.

## lowes_miloranite.py and homedepot_milorganite.py
I wanted to automatically check the inventory of Milorganite at my local home improvement stores. These scripts will check the local inventory and determine if it's in stock or not.

Each script can be modified to check inventory for different products and stores.
