#!/usr/bin/python

from socket import *
import Adafruit_BMP.BMP280 as BMP280
sensor= BMP280.BMP280(address=0x76)

temp = int(sensor.read_temperature()*9/5+32)
press = int(sensor.read_pressure()/10)

# APRS-IS login info
serverHost = 'mexico.aprs2.net'
serverPort = 14580
aprsUser = 'XE1REB-10'
aprsPass = '24503'

# APRS packet
callsign = 'FW9275'
btext1=("!2108.15N/10139.42W_000/000g000t0")
btext3=("r000p000P000h50b0")
btext5=("Pi3BMP280")
btext = btext1+str(temp)+btext3+str(press)+btext5

# create socket & connect to server
sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((serverHost, serverPort))
# logon
sSock.send(('user %s pass %s vers Pi3BMP280\n' % (aprsUser, aprsPass) ).encode("utf-8"))
# send packet
sSock.send(('%s>APRS:%s\n' % (callsign, btext) ).encode("utf-8"))
# close socket
sSock.shutdown(0)
sSock.close()
