# Create global variables as a dictionary, used when logging sensors that give the unique id of the system (MAC address) and the experiment started.
# A python file is generated that is 'read' by the logging program.
import os

filename = '/home/pi/MVP/python/env.py'

def createVariables():
    var = "env={'mac':'b8:27:eb:9b:15:1e', 'exp':'experiment_1'}"
    saveVariables(var)

def saveVariables(var):
    #print(var)
    f = open(filename, 'w+')
    tmp='env='+str(var)
    f.write(tmp)
    f.close()    

    
