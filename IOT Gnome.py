import requests
import time

def getChannelJSON(Channel,APIkey): #Returns raw JSON data from channel 
	URL = "https://api.thingspeak.com/channels/"+Channel+"/feeds.json?api_key="+APIkey+"&results=2"
	response = requests.get(URL)
	return response.json()

def getChannel(Channel,APIkey): #Print out all the details of our Channel
	print("___ Channel Details ___")
	
	responseJSON = getChannelJSON(Channel,APIkey)
	
	print("Channel ID: "+str(responseJSON['channel']['id']))
	print("Channel Name: "+str(responseJSON['channel']['name']))
	print("Channel Description: "+str(responseJSON['channel']['description']))
	print("Field 1: "+str(responseJSON['channel']['field1']))
	print("Field 2: "+str(responseJSON['channel']['field2']))
	print("Field 3: "+str(responseJSON['channel']['field3']))
	print("Creation date: "+str(responseJSON['channel']['created_at']))
	print("Last updated: "+str(responseJSON['channel']['updated_at']))
	print("Last entry: "+str(responseJSON['channel']['last_entry_id']))

	time.sleep(3)
	print()
	print("Type in a number! \n 0. Exit \n 1. Channel Details \n 2. Latest Entry \n 3. Live Update (Current + 5 Next Entries)")

def getFeed(Channel, APIkey, feedNumber):	#Print out all the details of our specific feed
	responseJSON = getChannelJSON(Channel,APIkey)									
	
	print("___Entry ID "+str(responseJSON['feeds'][feedNumber]['entry_id'])+"___")
	print("Entry created at: "+str(responseJSON['feeds'][feedNumber]['created_at']))
	print("Temperature: "+str(responseJSON['feeds'][feedNumber]['field1']))
	print("Humidity: "+str(responseJSON['feeds'][feedNumber]['field2']))
	print("Light Level: "+str(responseJSON['feeds'][feedNumber]['field3']))

def getLatestEntry(Channel, APIkey):
	responseJSON = getChannelJSON(Channel,APIkey)
	latest = str((responseJSON['channel']['last_entry_id']))					#Get latest entry id from channel JSON
	feedNumber = 0	
	
	while(responseJSON['feeds'][feedNumber]):									#while existing response
		if (int(latest) == int(responseJSON['feeds'][feedNumber]['entry_id'])):	#look for matching latest entry id
			getFeed(Channel,APIkey,feedNumber)									#print feed
			break

		feedNumber=feedNumber+1													#increment feed search

def checkEntryNumber(Channel,APIkey):
	responseJSON = getChannelJSON(Channel,APIkey)				#get JSON file
	latest = str((responseJSON['channel']['last_entry_id']))	#read through JSON file for entry id
	return latest												#returns last entry id

def liveUpdate(Channel,APIkey):
	firstUpdate = checkEntryNumber(Channel,APIkey)		#Check first update number
	getLatestEntry(Channel,APIkey)						#Print first update
	n=0													#Initial outputs
	while True:
		time.sleep(1)									#Wait 1 second before looping
		secondUpdate = checkEntryNumber(Channel,APIkey) #Check entry number

		if firstUpdate != secondUpdate:					#Check if the Entry number has changed
			print()
			getLatestEntry(Channel,APIkey)				#Prints out the newest update
			print()
			firstUpdate = secondUpdate					#Replaces firstUpdate with the secondUpdate for next loop
			n=n+1										#Updates the current number of updates
			if n == 5: 									#Number entries to break
				break	

	time.sleep(3)
	print()
	print("Type in a number! \n 0. Exit \n 1. Channel Details \n 2. Latest Entry \n 3. Live Update (Current + 5 Next Entries)")

def main():
	RAPIkey = #APIKey provided by ThingSpeak Here		 	#ReadKey: Key not needed for public channels
	Channel = #ThingSpeak Channel Number Here				#Channel # to our ThingSpeak

	print("___Main Menu___: Type in a number! \n 0. Exit \n 1. Channel Details \n 2. Latest Entry \n 3. Live Update (Current + 5 Next Entries)")
	
	while 1:									#Looping Menu
		print()
		userInput = str(input())
		print()
		if (userInput == "0"):
			print("Exiting...\n")
			break

		elif (userInput == "1"):
			getChannel(Channel,RAPIkey)

		elif (userInput == "2"):
			getLatestEntry(Channel, RAPIkey)

		elif (userInput == "3"):
			liveUpdate(Channel,RAPIkey)

		else:
			print("Error: Not an option.")

if __name__ == "__main__":
	main()
