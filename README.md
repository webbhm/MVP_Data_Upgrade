# MVP_Data_Upgrade
Add MAC address and environment to all records
This upgrade prepares your data for merging to the cloud CouchDB along with other users data.  The unique id (MAC) makes it possible to distinguish the data from one MVP from another.

Make a copy of your SD card, there is a slight risk of corrupting you data in CouchDB.

Copy all the files in the python directory to the MVP/python directory, over-writing the logData.py file (the others are new).

If you want to test this process before commiting to your actual data, copy CouchUpgradeData.py to another name, then:
* change the database name to something else ('test_upgrade')
* uncomment the line to create the database
* uncomment the line to create dummy data

Run the file CouchUpgradeData.py, either within the Python IDE, or from the command line
>>python CouchUpgradeData.py

This file will:
 * get your MAC address and put in in the env.py file
 * update your mvp_sensor_data database, adding the mac and experiment number information to each record
 * make a replication database (mvp_sensor_data_rep)
 * copy mvp_sensor_data to another table (getting rid of all the replication copies)
 * delete mvp_sensor_data database (getting rid of all the old data)
 * rebuild a new mvp_sensor_data database
 * copy the data back
 * add the view document to the database
 
 The new logData.py file will write the mac address and experiment number to each new log record from now on.
