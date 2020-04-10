data = "R1 68/51 37/8 48/0R2 26/11 24/0 26/0R3 19/13 20/1 15/0R4 49/34 56/3 61/2R5 27/23 30/7 44/0R6 27/18 48/9 24/1R7 50/41 28/5 42/0R8 45/30 19/5 55/0"

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

data_noR = data
for i in find(data, "R"):
	data_noR = data_noR[:i] + "  " + data[i+2:]

data_pipes = data_noR.replace("   ", "|")
data_pipes = data_pipes.replace(" ", "|")
data_split = data_pipes.split("|")[1:]
print(data_split)

sums = [[0, 0],[0, 0],[0, 0]]
index = 0
for i in data_split:
	data = i.split("/")
	sums[index][0]+= int(data[0])
	sums[index][1]+= int(data[1])
	index+=1
	if index == 3: index = 0

avgs = sums

avgs[0][0]/=8
avgs[0][1]/=8
avgs[1][0]/=8
avgs[1][1]/=8
avgs[2][0]/=8
avgs[2][1]/=8 

print(avgs)