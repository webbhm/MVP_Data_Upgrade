from datetime import tzinfo, datetime
import requests
import json
import env


#Output to file
def logData(name, status, attribute, value, comment):
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow())
    logFile(timestamp, name, status, attribute, value, comment)
    logDB(timestamp, name, status, attribute, value, comment)
    
def logFile(timestamp, name, status, attribute, value, comment):
    f = open('/home/pi/MVP/data/data.txt', 'a')
    s= timestamp + ", " + name + ", " + status + ", " + attribute + ", " + value + "," + comment + "," + env.env['mac'] + "," + env.env['exp'] + "\n"
    print(s)
    f.write(s)
    f.close()

def logDB(timestamp, name, status, attribute, value, comment):
    log_record = {
            'timestamp' : timestamp,
            'name' : name,
            'status' : status,
            'attribute' : attribute,
            'value' : value,
            'comment' : comment,
            'env' : env.env['mac'],
            'exp' : env.env['exp']
            }
    json_data = json.dumps(log_record)
    print json.dumps(log_record, indent=4, sort_keys=True)
    headers = {'content-type': 'application/json'}
    r = requests.post('http://localhost:5984/mvp_sensor_data', data = json_data, headers=headers)
    print r.json()

#Uncomment to test this function
#logData('si7021-top', 'Success', 'temperature', '27', '')    
