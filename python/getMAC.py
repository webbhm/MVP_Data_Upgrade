def getMAC(interface='wlan0'):
    # Return the MAC address of the interface
    try:
        str = open('/sys/class/net/' + interface + '/address').read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]

#print(getMAC('eth0'))
#print(getMAC('wlan0'))                   
                   
