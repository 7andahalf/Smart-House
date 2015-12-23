
import hotel,admins,users,db

'''
This script creates dummy data in the server
'''

devices = db.database("devices")

# Create some devices to test with

devices.addColumn("deviceID")
devices.addColumn("name")
devices.addColumn("type")
devices.addColumn("parent")
devices.addColumn("status")
devices.addColumn("lastModified")
devices.addColumn("others")

# Doors
devices.insert({
		'deviceID' : '1',
		'name' : 'The main door',
		'type' : 'door',
		'parent' : 'house',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '2',
		'name' : 'Tubelight #1',
		'type' : 'light',
		'parent' : 'house',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '3',
		'name' : 'Bulb #1',
		'type' : 'light',
		'parent' : 'house',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

print "Devices: done"
print db.database("util").data
print ""