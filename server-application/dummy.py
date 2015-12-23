import db
'''
This script creates dummy data in the server
'''

devices = db.database("devices")
rooms = db.database("rooms")

# Create some rooms

rooms.addColumn("roomID") # unique ID of the room
rooms.addColumn("name")   # name of the room
rooms.addColumn("floor")  # floor in which the room is present
rooms.addColumn("type")   # type of room ex: bedroom, bathroom etc

rooms.insert({
		'roomID' : '1',
		'name' : 'Entry room',
		'floor' : 'G',
		'type' : 'entry'
	})

rooms.insert({
		'roomID' : '2',
		'name' : 'Hall',
		'floor' : 'G',
		'type' : 'living'
	})

rooms.insert({
		'roomID' : '3',
		'name' : 'Kitchen',
		'floor' : 'G',
		'type' : 'kitchen'
	})

rooms.insert({
		'roomID' : '4',
		'name' : 'Master bedroom',
		'floor' : 'G',
		'type' : 'bedroom'
	})

rooms.insert({
		'roomID' : '5',
		'name' : 'Guest bedroom',
		'floor' : 'G',
		'type' : 'bedroom'
	})

rooms.insert({
		'roomID' : '6',
		'name' : 'pantry',
		'floor' : 'G',
		'type' : 'storage'
	})

rooms.insert({
		'roomID' : '7',
		'name' : 'Staircase',
		'floor' : 'G',
		'type' : 'others'
	})

rooms.insert({
		'roomID' : '8',
		'name' : 'Staircase',
		'floor' : '1',
		'type' : 'others'
	})

rooms.insert({
		'roomID' : '9',
		'name' : 'garden',
		'floor' : 'G',
		'type' : 'outside'
	})

print "Rooms: done"
print db.database("rooms").data
print ""

# Create some devices to test with

devices.addColumn("deviceID")
devices.addColumn("name")
devices.addColumn("type")
devices.addColumn("parent")
devices.addColumn("status")
devices.addColumn("lastModified")
devices.addColumn("others")

# Entry room
devices.insert({
		'deviceID' : '1',
		'name' : 'The main door',
		'type' : 'door',
		'parent' : '1',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '2',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '1',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Hall
devices.insert({
		'deviceID' : '3',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '2',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '4',
		'name' : 'Tube light #1',
		'type' : 'light',
		'parent' : '2',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '5',
		'name' : 'Tube light #2',
		'type' : 'light',
		'parent' : '2',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '6',
		'name' : 'Fan',
		'type' : 'fan',
		'parent' : '2',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '7',
		'name' : 'TV',
		'type' : 'tv',
		'parent' : '2',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Kitchen
devices.insert({
		'deviceID' : '8',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '3',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '9',
		'name' : 'Tube light #1',
		'type' : 'light',
		'parent' : '3',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '10',
		'name' : 'exhaust',
		'type' : 'others',
		'parent' : '3',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Master bedroom
devices.insert({
		'deviceID' : '11',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '4',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '12',
		'name' : 'Tube light #1',
		'type' : 'light',
		'parent' : '4',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '13',
		'name' : 'Tube light #2',
		'type' : 'light',
		'parent' : '4',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '14',
		'name' : 'Fan',
		'type' : 'fan',
		'parent' : '4',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '15',
		'name' : 'TV',
		'type' : 'tv',
		'parent' : '4',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Guest bedroom

devices.insert({
		'deviceID' : '16',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '5',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '17',
		'name' : 'Tube light #1',
		'type' : 'light',
		'parent' : '5',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '18',
		'name' : 'Fan',
		'type' : 'fan',
		'parent' : '5',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Pantry

devices.insert({
		'deviceID' : '19',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '6',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Staircase

devices.insert({
		'deviceID' : '20',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '7',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '21',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '8',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

# Garden

devices.insert({
		'deviceID' : '22',
		'name' : 'Bulb',
		'type' : 'light',
		'parent' : '9',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

devices.insert({
		'deviceID' : '23',
		'name' : 'Sprinklers',
		'type' : 'others',
		'parent' : '9',
		'status' : None,
		'lastModified' : None,
		'others' : []
	})

print "Devices: done"
print db.database("devices").data
print ""