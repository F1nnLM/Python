from options import Options
from time import *
from physical import *
from gpio import *
from ioeclient import IoEClient


DELAY_TIME = 1000        # var DELAY_TIME
current_time = 0        # var current_time

X_READ_DISTANCE = 50        # var X_READ_DISTANCE
Y_READ_DISTANCE = 50        # var Y_READ_DISTANCE
cardID = 0        # var cardID
lastCardID = 0        # var lastCardID
state = 2 # waiting        # var state


def setup ():

    # Registration Server Setup
    
    IoEClient.setup({
        "type": "RFID Reader",
        "states": [{
                "name": "Card ID",
                "type": "number",
                "unit": '',
                "controllable": False
            },
            {
                "name": "Status",
                "type": "options",
                "options": {
                    "0": "Valid",
                    "1": "Invalid",
                    "2": "Waiting"
                },
                "controllable": True
        }]
    })
    
    IoEClient.onInputReceive( lambda rinput: processData(rinput, True) )



def loop ():
    global cardID, lastCardID, state
    devices = devicesAt(getCenterX(), getCenterY(), X_READ_DISTANCE, Y_READ_DISTANCE)        # var devices
    found = False        # var found
    for i in xrange(0, len(devices)) :
        if devices[i] is getName():
            continue

        cardID = getDeviceProperty(devices[i], 'CardID')
        found = True
        break
#reading the card
    if not found:
        cardID = lastCardID = 0
        digitalWrite(0,LOW)
        setState(2)
    else:
        if lastCardID != cardID:
            lastCardID = cardID
            sendReport()
            if (cardID == "1001"):
            	digitalWrite(0,HIGH)
            	setState(0)
            else:
		digitalWrite(0,LOW)
		setState(1)
				
	
	delay(DELAY_TIME)

def setState (newState):
    global  state
    if state != newState:
        state = newState
        analogWrite(A1, state)
        sendReport()

def sendReport ():
	report  = str( int(cardID)) + "," + str(state)        # var report
	IoEClient.reportStates(report)
	
def processData (data, bIsRemote):
	if len(data) <= 0:
		return
	data = data.split(",")
	setState(int(data[1]))

if __name__ == "__main__":
	setup()
	while True:
		loop()
		idle()
