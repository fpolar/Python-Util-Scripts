import time
import sys

shot1 = {"text": "shot1",  "prio":1, "dur":200, "st":5100}
shot1_2 = {"text": "shot1_2",  "prio":2, "dur":200, "st":5100}
shot2 = {"text": "shot2",  "prio":2, "dur":200, "st":5200}
shot3 = {"text": "shot3",  "prio":3, "dur":200, "st":5300}
shot4 = {"text": "shot4",  "prio":4, "dur":200, "st":5400}
shot5 = {"text": "shot5",  "prio":2, "dur":200, "st":5800}
shot6_lowprio = {"text": "shot6_lowprio",  "prio":1, "dur":200, "st":5800}

shots = [shot3, shot1, shot1_2, shot2, shot4, shot5, shot6_lowprio]
shotsSorted = sorted(shots, key = lambda i: i["st"])

# curr_messages_index = 0
# This is unused now, but we can use this to later make
# searching for the next message to display more efficient

currMessage = "No Message"
currDuration = sys.maxsize
currPrio = 0
timer = 5350
while shotsSorted:

	if currDuration <= 0:
		currMessage = "No Message"
		currDuration = sys.maxsize
		currPrio = 0

	for i in range(0, len(shots)):
		if timer >= shotsSorted[i]["st"] and \
		timer < shotsSorted[i]["st"]+shotsSorted[i]["dur"] and\
		shotsSorted[i]["prio"]>currPrio:
			currMessage = shotsSorted[i]["text"]
			currDuration = shotsSorted[i]["dur"]
			currPrio = shotsSorted[i]["prio"]


	sys.stdout.write("\r")
	# sys.stdout.write("{} - {} - {}          ".format(timer, currMessage, currDuration))
	sys.stdout.write("{} - {}          ".format(timer, currMessage))
	sys.stdout.flush()
	timer+=1
	currDuration-=1
	time.sleep(.1)