#!/usr/bin/env python3

import ipaddress

class Switch:
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return self.name
  def __setattr__(self, name, value):
    localdebug = False
    ip_test = ipaddress.ip_address('192.168.1.1')
    if name == "ip" and type(value) != type(ip_test):
      print("IP address is not an IP address, "+value)
    else:
      super().__setattr__(name, value)
      if localdebug == True: print(name+","+value+","+str(value))
      pass
  name = ""
  ip = ipaddress.ip_address('192.168.1.1')
  ports = []
  def new_port(self, slot, port):
    port = SwitchPort(slot,port)
    self.ports.append(port)

class SwitchPort:
  def __init__(self, slot, port):
    self.slot = slot
    self.port = port
  def 
  slot = ""
  port = ""
  description = ""

#switch1 = Switch('sw1')
#switch1.ip=ipaddress.ip_address("134.121.1.1")
#switch2 = Switch('sw2')
#switch2.ip=ipaddress.ip_address("129.101.1.1")

#switches={}
#switches['swit1']=switch1
#switches['swit2']=switch2

#for switch in switches:
#  print(switches[switch])
