# Replicates a database and gets rid of old versions (and version number)
# Deletes database and replicates back
# Remove tempory working database
import couchdb
import env
import json
from getMAC import getMAC
from saveEnv import setEnv

doc={"_id":"_design/doc","language":"javascript","views":{"attribute_value":{"map":"function(doc) {\n\t\tif(doc.value && doc.attribute && doc.status == 'Success')\n\t   \t{\n\t\t\temit([doc.attribute, doc.name, doc.timestamp], doc);\n\t   \t}\n}"}}}



def tableClean(db_name):
    '''Gets rid of the extra records created from the update'''
    dup_name = db_name + "_dup"

    # open existing table
    db = couch[db_name]
    # create temp table
    dup = couch.create(dup_name)

    # Replicate
    print("Replicate db to dup")
    for key in db:
    #    print(key)
        doc=db.get(key)
        del doc["_rev"]
        dup.save(doc)

    # Delete first database
    print("Delete db")
    del couch[db_name]

    # Rebuild first database
    print("Rebuild db")
    db = couch.create(db_name)

    # Replicate back
    print("Replicate dup to db")
    for key in dup:
    #    print(key)
        doc=dup.get(key)
        del doc["_rev"]    
        db.save(doc)

    # Delete tmp database
    print("Delete dup")
    del couch[dup_name]        

    print("Done")

def upgradeTable(db_name):
    '''Add MAC address and experiment identifier to each record'''

    db = couch[db_name]
    # Update 1 - add MAC address
    print("Update 1")
    for key in db:
    #    print(key)
        doc=db.get(key)
    #    print(doc)
        doc['env']=env.env['mac']
    #    print(doc)
        db.save(doc)

    # Update 2 - add experiment id
    print("Update 2")
    for key in db:
    #    print(key)
        doc=db.get(key)
    #    print(doc)
        doc['exp']=env.env['exp']
    #    print(doc)
        db.save(doc)

def addDoc(db_name, doc):
    db=couch[db_name]
    db.create(doc)

def createDummy(db_name):
    print("Create records")
    db=couch[db_name]
    for x in range(0,13):
        data={'foo':0, 'bar':'a'}
        data['foo']=x
        db.save(data)    
    

# Get this mac address
mac=getMAC()
setEnv('mac', mac)

#Upgrade data
db_name='mvp_sensor_data'
couch = couchdb.Server()
#db = couch.create(db_name)
#createDummy(db_name)
upgradeTable(db_name)
tableClean(db_name)
#add view doc back in
addDoc(db_name, doc)


