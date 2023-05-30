import random
import os

# ask for the file
os.system("mode con lines=36")
os.system('cls')
print('Here are the files you can choose from:')
weather_files = os.listdir('./weather/')
print('')
for i in weather_files:
	if i != "weather gen":
		print("\t{}".format(i))
temp = input("\nPlease enter the file name: ")
# if there is none specified use the default
if temp == "":
	file = "weather/arctic_forest_weather_5year.csv"
else:
	# otherwise make sure that there is a .csv
	if ".csv" in temp:
		file = temp
	else:
		file = 'weather/{}.csv'.format(temp)


with open(file) as f:
	f = f.readlines()
for i in range(0,len(f)):
	f[i] = f[i].replace("\n","")
	f[i] = f[i].split(",")
f.pop(0)

def display(rain,wind_max,day,weekday,month,monthday,\
	hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
	wind_low,wind_missile,wind_melee,wind_move,viz_day,\
	viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season):
	
	dawn, dusk, dl = daylight(day,climate)

	for i in range(0,25-len(rain)):
		rain +=" "
	for i in range(0,4-len(eff_hi)):
		eff_hi = " " + eff_hi
	for i in range(0,4-len(eff_lo)):
		eff_lo = " " + eff_lo
	for i in range(0,25-len(spec)):
		spec += " "
	for i in range(0,4-len(hi)):
		hi = " " + hi
	for i in range(0,4-len(lo)):
		lo = " " + lo
	if len(monthday) < 2:
		monthday = " " + monthday
	for i in range(0,13-len(month)):
		month += " "
	for i in range(0,4-len(day)):
		day = " " + day
	viz_day += " yds"
	viz_twi += " yds"
	viz_moon += " yds"
	viz_dark += " yds"
	for i in range(0,10-len(viz_day)):
		viz_day += " "
	for i in range(0,10-len(viz_twi)):
		viz_twi += " "
	for i in range(0,10-len(viz_moon)):
		viz_moon += " "
	for i in range(0,10-len(viz_dark)):
		viz_dark += " "
	wind_max += " mph"
	for i in range(0,11-len(wind_max)):
		wind_max += " "
	for i in range(0,20-len(winddir)):
		winddir += " "
	for i in range(0,11-len(wind_missile)):
		wind_missile += " "
	for i in range(0,11-len(wind_melee)):
		wind_melee += " "
	for i in range(0,11-len(wind_move)):
		wind_move += " "
	humiditymod += "%"
	for i in range(0,4-len(humiditymod)):
		humiditymod += " "

	for i in range(0,31-len(wilderness[0][1])):
		wilderness[0][1] += " "
	for i in range(0,31-len(wilderness[1][0])):
		wilderness[1][0] += " "
	for i in range(0,31-len(wilderness[1][1])):
		wilderness[1][1] += " "
	for i in range(0,31-len(wilderness[1][2])):
		wilderness[1][2] += " "
	for i in range(0,31-len(wilderness[1][3])):
		wilderness[1][3] += " "
	for i in range(0,18-len(wilderness[2][1])):
		wilderness[2][1] += " "
	for i in range(0,18-len(wilderness[2][2])):
		wilderness[2][2] += " "
	for i in range(0,18-len(wilderness[2][3])):
		wilderness[2][3] += " "
	for i in range(0,3-len(wilderness[3][0])):
		wilderness[3][0] += " "
	for i in range(0,18-len(wilderness[3][1])):
		wilderness[3][1] += " "
	for i in range(0,18-len(wilderness[5][1])):
		wilderness[5][1] += " "
	for i in range(0,18-len(wilderness[5][2])):
		wilderness[5][2] += " "
	for i in range(0,13-len(wilderness[4])):
		wilderness[4] += " "
	for i in range(0,24-len(wilderness[6])):
		wilderness[6] += " "
	for i in range(0,10-len(climate)):
		climate += " "
	for i in range(0,10-len(terrain)):
		terrain += " "
	for i in range(0,10-len(season)):
		season += " "
	for i in range(0,4-len(dl)):
		dl = " " + dl

	os.system('cls')
	print('═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
	print('this program is reading from : {}'.format(file))
	print('')
	print('                                             Current Conditions')
	print('┌───────────────────────────┬───────────┐ ┌──────────────────────┐ ┌─────────────────────────────────┐')	# 1
	print('│       weather   hum: {} │   hi   lo │ │         wind         │ │     surrounding wilderness      │'.format(humiditymod))	# 2
	print('├───────────────────────────┼───────────┤ ├──────────────────────┤ ├─────────────────────────────────┤')	# 3
	print('│ {} │ {} {} │ │          {} │ │ hunt                            │'.format(rain,eff_hi,eff_lo,wind_max))	# 4
	print('│ {} │ {} {} │ │ {} │ │ {} │'.format(spec,hi,lo,winddir,wilderness[0][1]))	# 5
	print('└───────────────────────────┴───────────┘ │                      │ │                                 │')	# 6
	print('            ┌───────────────────────────┐ │ missiles {} │ │ fish                            │'.format(wind_missile))	# 7
	print(' {} │ {} {}  (d {})│ │    melee {} │ │ {} │'.format(climate,monthday,month,day,wind_melee,wilderness[1][0]))	# 8
	print(' {} ├───────────────────────────┤ │     move {} │ │ {} │'.format(terrain,wind_move,wilderness[1][1]))	# 9
	print(' {} │            day {} │ └──────────────────────┘ │ {} │'.format(season,viz_day,wilderness[1][2]))	# 10
	print('            │       twilight {} │ ┌──────────────────────┐ │ {} │'.format(viz_twi,wilderness[1][3]))		# 11
	print(' dawn {} │      moonlight {} │ │     morale checks    │ │                                 │'.format(dawn,viz_moon))		# 12
	print(' dusk {} │           dark {} │ ├──────────────────────┤ │ forage                          │'.format(dusk,viz_dark))		# 13
	print(' ({} h)   └───────────────────────────┘ │ surprised            │ │      found : {} │'.format(dl,wilderness[2][1]))		# 14
	print('           ┌────────────────────────────┐ │ superior force       │ │ prof found : {} │'.format(wilderness[2][2]))
	print('           │      water min (pints)     │ │ ally slain by magic  │ │    problem : {} │'.format(wilderness[2][3]))
	print('           ├────────────────────────────┤ │ 1/4 group fallen     │ │                                 │')
	print('           │          <50  <70  <90   + │ │ 1/2 group fallen     │ │ water : {}, {} │'.format(wilderness[3][0],wilderness[3][1]))
	print('           │ inactive   5    6    7   8 │ │ " " " & ally falls   │ │                                 │')
	print('           │    light   6    7    8  10 │ │ tempted (bribe, &c)  │ │ medicinal plant                 │')
	print('           │ moderate   8    9   10  12 │ │ covering rear guard  │ │      found : {} │'.format(wilderness[5][1]))
	print('           │    heavy   9   10   12  16 │ │ use magic charge     │ │ prof found : {} │'.format(wilderness[5][2]))
	print('           └────────────────────────────┘ │ surrounded           │ │                                 │')
	print('                                          └──────────────────────┘ │ natural shelter : {} │'.format(wilderness[4]))
	print('                                                                   │ fuel : {} │'.format(wilderness[6]))
	print('                                                                   └─────────────────────────────────┘')
	print('')


# hunting
def hunting(climate, terrain, season):
	# map -> biome -> terrain -> season
	huntmap = [
		[[5,5,10,5],[5,5,10,10],[5,5,10,10],[5,5,5,5],[5,10,10,5],[5,10,10,5],[5,10,10,5]], # arctic
		[[5,10,10,5],[5,10,10,5],[5,10,15,15],[5,5,10,5],[5,10,15,15],[5,15,20,20],[5,10,15,10]], # subarctic
		[[10,5,5,10],[30,50,50,50],[25,50,50,50],[15,30,30,30],[25,40,50,50],[20,40,50,50],[20,35,50,50]], # temperate
		[[10,5,5,5],[50,50,50,50],[50,50,50,50],[35,35,35,35],[50,50,50,50],[50,50,50,50],[40,50,50,50]], # subtropical
		[[5,5,5,5],[50,50,50,50],[50,50,50,50],[40,40,40,40],[50,50,50,50],[50,50,50,50],[50,50,50,50]]  # tropical
	]

	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	climate = climates.index(climate)
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	encountered_game = "No"
	huntdist = " "
	if random.randint(0,99) < huntmap[climate][terrain][season]:
		encountered_game = "Yes"

		# distance of creatures encountered
		x = random.randint(1,6)
		a = ['S','S','M','M','M','L']
		if x == 1:
			b = random.randint(1,6) + random.randint(1,6)
			c = random.randint(2,4) * 10
		elif x == 2:
			b = random.randint(1,6)
			c = random.randint(2,4) * 10
		elif x == 3:
			b = random.randint(1,10)
			c = random.randint(2,4) * 10
		elif x == 4:
			b = random.randint(1,6)
			c = random.randint(4,6) * 10
		elif x == 5:
			b = random.randint(1,3)
			c = random.randint(4,6) * 10
		elif x == 6:
			b = random.randint(1,3)
			c = random.randint(6,8) * 10
		
		huntdist = "{} size, {} creatures at {} yards".format(a[x-1],b,c)

	return([encountered_game,huntdist])

# fishing chance
def fish(climate, terrain, season):
	output = ["    dawn/day/dusk/night"]
	poor_dawn = random.randint(1,4)+2 
	poor_day  = random.randint(1,4)-2
	poor_dusk = random.randint(1,4)+2
	poor_night= random.randint(1,4)
	fair_dawn = random.randint(1,6)+2 
	fair_day  = random.randint(1,6)-3
	fair_dusk = random.randint(1,6)+2
	fair_night= random.randint(1,6)-1
	good_dawn = random.randint(1,8)+2
	good_day  = random.randint(1,6)-2
	good_dusk = random.randint(1,8)+2
	good_night= random.randint(1,6)+2
	output.append("poor: {} / {} / {} / {}".format(poor_dawn,poor_day,poor_dusk,poor_night))
	output.append("fair: {} / {} / {} / {}".format(fair_dawn,fair_day,fair_dusk,fair_night))
	output.append("good: {} / {} / {} / {}".format(good_dawn,good_day,good_dusk,good_night))
	return(output)

# foraging chance
def forage(climate, terrain, season):
	foragemap = [
	[[0,5,10,0],[5,10,10,5],[5,10,10,5],[0,0,5,0],[5,5,10,5],[10,10,15,10],[10,10,15,10]],
	[[0,5,15,5],[70,85,100,75],[20,30,40,25],[10,15,20,15],[20,30,50,25],[25,35,50,35],[15,20,30,50]],
	[[10,5,5,5],[80,90,100,90],[65,75,90,80],[20,30,40,30],[50,60,75,60],[50,65,80,65],[30,35,40,35]],
	[[5,5,0,5],[90,100,100,100],[80,90,100,95],[40,55,75,60],[80,90,100,100],[80,90,100,95],[40,50,50,50]],
	[[5,5,0,5],[100,100,100,100],[90,100,100,95],[85,90,90,90],[100,100,100,100],[90,95,100,95],[50,60,70,60]]
	]
	ediblemap = [
	[[0,75,75,0],[75,60,60,50],[75,60,60,50],[0,0,50,0],[50,50,50,50],[75,70,70,75],[75,70,70,75]],
	[[0,50,50,75],[40,40,50,40],[50,50,40,50],[50,50,40,50],[40,4,40,50],[60,50,40,50],[60,60,60,50]],
	[[70,50,70,50],[40,40,40,40],[50,40,35,50],[40,40,40,50],[40,40,30,50],[50,40,40,50],[60,50,50,60]],
	[[75,80,0,75],[30,30,30,30],[30,30,25,25],[40,30,30,40],[30,30,30,35],[40,40,40,40],[60,50,50,60]],
	[[75,80,0,75],[30,30,40,30],[30,40,40,35],[30,30,40,35],[30,45,50,40],[40,50,50,50],[60,60,50,60]]
	]
	# the forage map is the percent chance that a normal character foraging 
	# for 2 turns will find one full day's ration of plant life (2 lbs)
	# the edible map is the percent chance that what they find is 
	# actually not edible
	# with proficiency in foraging, they find 4 lbs of food
	# and the chance of inedible is 20% less
	
	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	climate = climates.index(climate)
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	foragechance = foragemap[climate][terrain][season]
	ediblechance = ediblemap[climate][terrain][season]

	forageroll = random.randint(0,99)
	edibleroll = random.randint(0,99)

	foundfood = "None"
	ediblefood = "None"
	profediblefood = "None"
	foodproblem = "None"

	if forageroll < foragechance:
		foundfood = "yes"
		if edibleroll > ediblechance:
			ediblefood = "edible"
		if edibleroll + 20 > ediblechance:
			profediblefood = "edible"

	if ediblefood == 'None':
		foodproblem = random.choice(['poisonous','poisonous','spoiled','tainted','spoiled','not nutritious','not nutritious','not nutritious','not nutritious'])

	return([foundfood, ediblefood, profediblefood, foodproblem])

# finding water chance
def water(climate, terrain, season):
	watermap = [
	[[5,5,5,5],[10,10,10,10],[10,10,10,10],[5,5,5,5],[10,10,10,10],[10,10,10,10],[10,10,10,10]],
	[[5,10,10,5],[10,20,20,10],[5,10,15,10],[5,20,15,10],[10,20,20,15],[40,60,50,50],[40,60,50,50]],
	[[5,5,5,5],[30,40,30,30],[30,40,40,30],[20,20,15,20],[20,40,40,30],[60,70,80,60],[60,70,80,60]],
	[[5,5,5,5],[60,70,70,60],[30,50,50,40],[40,60,50,40],[20,40,30,20],[70,80,90,70],[70,80,90,70]],
	[[5,10,5,5],[80,80,80,80],[15,20,30,15],[40,70,60,70],[20,50,60,50],[70,90,90,80],[70,90,90,80]]
	]
	undrinkablemap = [
	[[50,50,50,50],[50,50,50,50],[50,50,50,50],[30,30,30,30],[50,50,50,50],[50,50,50,50],[50,50,50,50]],
	[[60,60,60,60],[40,40,50,40],[40,40,50,40],[30,30,30,30],[50,50,50,50],[60,60,60,60],[60,60,60,60]],
	[[70,70,70,80],[30,30,30,30],[40,40,50,40],[30,30,30,30],[5,50,5,50],[70,70,80,70],[70,70,80,70]],
	[[70,70,80,80],[40,50,60,50],[40,40,40,40],[30,40,50,40],[50,40,40,50],[70,70,80,80],[70,70,80,80]],
	[[70,70,80,80],[50,60,70,60],[40,40,50,40],[30,30,40,40],[50,50,60,50],[70,75,80,80],[70,75,80,80]]
	]

	
	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	climate = climates.index(climate)
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	foundwater = "No"
	waterquality = "Clean"

	if random.randint(0,99) < watermap[climate][terrain][season]:
		foundwater = "Yes"
		if random.randint(0,99) < undrinkablemap[climate][terrain][season]:
			waterquality = "Tainted"

	return([foundwater,waterquality])

# chance of finding natural shelter
def naturalshelter(climate, terrain, season):
	sheltermap = [
	[20,20,20,20],
	[90,100,100,100],
	[40,60,70,60],
	[40,40,40,40],
	[30,40,40,30],
	[40,50,50,40],
	[40,50,50,40]
	]

	
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	foundshelter = "No"

	if random.randint(0,99) < sheltermap[terrain][season]:
		foundshelter = "Yes"

	return(foundshelter)

# chance of finding medicinal plants
def medicinalplant(climate, terrain, season):
	medicinalmap = [
	[[0,5,10,0],[5,10,10,5],[5,10,10,5],[0,0,5,0],[5,5,10,5],[10,10,15,10],[10,10,15,10]],
	[[0,5,15,5],[70,85,100,75],[20,30,40,25],[10,15,20,15],[20,30,50,30],[25,35,50,35],[15,20,30,20]],
	[[10,5,5,5],[80,90,100,90],[65,75,90,80],[20,30,40,30],[50,60,75,60],[50,65,80,65],[30,35,40,35]],
	[[5,5,0,5],[90,100,100,100],[80,90,100,95],[40,55,75,60],[80,90,100,100],[80,90,100,95],[40,50,50,50]],
	[[5,5,0,5],[100,100,100,100],[90,100,100,95],[85,90,90,90],[100,100,100,100],[90,95,100,95],[50,60,70,60]]
	]
	usablemap = [
	[[0,10,10,0],[10,10,10,10],[10,10,10,10],[0,0,20,0],[20,20,20,20],[10,20,20,10],[10,20,20,10]],
	[[0,10,10,10],[30,30,20,30],[20,20,30,20],[20,20,30,20],[20,30,30,20],[10,20,30,20],[10,10,10,20]],
	[[10,10,10,20],[30,30,30,30],[20,30,40,20],[20,30,30,20],[20,30,40,20],[20,30,30,20],[10,20,20,10]],
	[[10,10,0,10],[40,40,40,40],[40,40,50,50],[30,40,40,30],[40,40,40,40],[30,30,30,30],[10,20,20,10]],
	[[10,10,0,10],[40,40,30,40],[30,30,30,30],[40,40,30,40],[40,40,40,30],[30,40,40,30],[10,10,20,10]]
	]

	# medicinal map is the chance of there being vegetation to search in
	# usable map is the chance of finding the plant

	
	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	climate = climates.index(climate)
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	suitablevegetation = "No"
	foundmedicine = "No"
	proffoundmedicine = "No"

	# see if there is suitable vegetation
	if random.randint(0,99) < medicinalmap[climate][terrain][season]:
		suitablevegetation = "Yes"
		medicineroll = random.randint(0,99)
		if medicineroll < usablemap[climate][terrain][season]/2:
			foundmedicine = "Yes"
		if medicineroll < usablemap[climate][terrain][season]:
			proffoundmedicine = "Yes"

	return([suitablevegetation,foundmedicine,proffoundmedicine])

# availability of fuel
def fuel(climate, terrain, season):
	fuelmap = [
	[20,20,20,20],
	[70,100,100,100],
	[40,70,70,60],
	[20,30,40,40],
	[50,70,80,70],
	[40,30,30,40],
	[40,30,30,40]
	]
	climatemodmap = [
	[-20,-10,0,-10,-20],
	[-100,-30,0,30,30],
	[-30,-20,0,10,20],
	[-40,-30,0,20,30],
	[-60,-40,0,20,20],
	[-40,-20,0,10,20],
	[-40,-20,0,10,20]
	]

	
	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	terrains = ['desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp']
	seasons = ['winter', 'spring', 'summer', 'fall']
	
	climate = climates.index(climate)
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	foundfuel = "No"
	fuelchance = fuelmap[terrain][season]
	climatemod = climatemodmap[terrain][climate]

	if random.randint(0,99) < fuelchance + climatemod:
		foundfuel = "Yes"

	return(foundfuel)

def surroundingwilderness(climate, terrain, season):

	a = hunting(climate, terrain, season)
	b = fish(climate, terrain, season)
	c = forage(climate, terrain, season)
	d = water(climate, terrain, season)
	e = naturalshelter(climate, terrain, season)
	f = medicinalplant(climate, terrain, season)
	g = fuel(climate, terrain, season)

	return([a,b,c,d,e,f,g])

# show surrounding plants
# spring summer fall winter
# arctic subarctic temperate subtropical tropical
# desert forest hill plains mountain swamp coast
def plants(climate, terrain, season):
	#season = ['spring', 'summer', 'fall', 'winter'].index(season)
	#climate = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical'].index(climate)
	#terrain = ['desert', 'forest', 'hill', 'plains', 'mountain', 'swamp', 'coast'].index(terrain)
	# summer/tropical/forest should be 64
	# 1, 4, 1
	with open("plants by area/_{}_{}_{}.txt".format(season,climate,terrain), "r") as tempfile:
		line = tempfile.readline()
	#print(line)
	plantslist = line
	plantslist = plantslist.split(", ")
	#print(plantslist)
	if len(plantslist) < 21:
		os.system('cls')
		print("┌────────────────────────────────┬──────────────────────────────────────────────────────────────┬──────┐")
		print("│ herb                           │ use                                                          │ enc. │")
		print("├────────────────────────────────┼──────────────────────────────────────────────────────────────┼──────┤")
		count = 0
		for i in plantslist:
			count += 1
			i = i.split(" | ")
			herb = i[0].replace("\"","")
			use = i[1]
			encumberance = i[2].replace("\"","")
			for j in range(0,30-len(herb)):
				herb += " "
			for j in range(0,60-len(use)):
				use += " "
			for j in range(0,4-len(encumberance)):
				encumberance += " "
			print("│ ",herb," │ ",use," │ ",encumberance, " │",sep="")
			if count%3 == 2:
				print("│--------------------------------│--------------------------------------------------------------│------│")
		print("└────────────────────────────────┴──────────────────────────────────────────────────────────────┴──────┘")
		x = input('press Enter to return')
	else:
		step = 20
		for i in range(0,len(plantslist),step):
			os.system('cls')
			a = i
			sub_plantslist = plantslist[a:a+step]
			print("┌────────────────────────────────┬──────────────────────────────────────────────────────────────┬──────┐")
			print("│ herb                           │ use                                                          │ enc. │")
			print("├────────────────────────────────┼──────────────────────────────────────────────────────────────┼──────┤")
			count = 0
			for i in sub_plantslist:
				count += 1
				i = i.split(" | ")
				herb = i[0].replace("\"","")
				use = i[1]
				encumberance = i[2].replace("\"","")
				for j in range(0,30-len(herb)):
					herb += " "
				for j in range(0,60-len(use)):
					use += " "
				for j in range(0,4-len(encumberance)):
					encumberance += " "
				print("│ ",herb," │ ",use," │ ",encumberance, " │",sep="")
				if count%3 == 2:
					print("│--------------------------------│--------------------------------------------------------------│------│")
			print("└────────────────────────────────┴──────────────────────────────────────────────────────────────┴──────┘")
			x = input('press Enter to continue')



# MORALE
def morale():
	print('')
	print('\t┌──────────────────────────────┬──────────────────────────────┐')
	print('\t│  a   abandoned by friends    │  n   1/2 HD                  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  b   3/4 hp                  │  o     1 HD                  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  c   1/2 hp                  │  p   4-8 HD                  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  d   creature is chaotic     │  q   9-14HD                  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  e   fighting hated enemy    │  r   15+ HD                  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  f   creature is lawful      │  s   leader diff alignment   │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  g   surprised               │  t   powerful ally killed    │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  h   fighting magic-users    │  u   treated well by leader  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  i   defending home          │  v   treated poor by leader  │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  j   terrain advantage       │  w   no enemy slain          │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print("\t│  k   can't affect opponent   │  x   magic-user ally         │")
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print('\t│  l   terrain advantage       │  y   outnumbered 3 to 1      │')
	print('\t├──────────────────────────────┼──────────────────────────────┤')
	print("\t│  m   can't affect opponent   │  z   outnumber 3 to 1        │")
	print('\t└──────────────────────────────┴──────────────────────────────┘')
	 
	x = input("\nEnter Check:    ")
	
	mod = 0
	
	if 'a' in x:
		mod += -6
	if 'b' in x:	
		mod += -2
	if 'c' in x:	
		mod += -4
	if 'd' in x:	
		mod += -1
	if 'e' in x:	
		mod += 4
	if 'f' in x:	
		mod += 1
	if 'g' in x:	
		mod += -2
	if 'h' in x:	
		mod += -2
	if 'i' in x:	
		mod += 3
	if 'j' in x:	
		mod += 1
	if 'k' in x:	
		mod += -8
	if 'l' in x:	
		mod += 1
	if 'm' in x:	
		mod += -2
	if 'n' in x:	
		mod += -1
	if 'o' in x:	
		mod += 1
	if 'p' in x:	
		mod += 2
	if 'q' in x:	
		mod += 3
	if 'r' in x:	
		mod += -1
	if 's' in x:	
		mod += -4
	if 't' in x:	
		mod += 2
	if 'u' in x:	
		mod += -4
	if 'v' in x:	
		mod += -2
	if 'w' in x:	
		mod += 2
	if 'x' in x:	
		mod += -4
	if 'y' in x:	
		mod += 2
	
	a = random.randint(1,10)
	b = random.randint(1,10)
	o = a + b + mod
	print('\t╔═══════════════╗')
	print('\t║\t{}\t║\t RESULT'.format(o))
	print('\t╚═══════════════╝')
	print('\t      [ {} ]\t\t DICE ROLLS\n\t     mod: {}'.format((a+b),mod))
	xyz = input('press Enter to return')

# INITIATIVE
def initiative():
	print('\t                      Initiative Modifers                      ')
	print('\t┌───────────────────────────────┬────────────────────────────────┐')
	print('\t│  0   hasted                   │  3   slowed                    │')
	print('\t├───────────────────────────────┼────────────────────────────────┤')
	print('\t│  1   on higher ground         │  4   wading/slippery footing   │')
	print('\t├───────────────────────────────┼────────────────────────────────┤')
	print('\t│  2   set to receive a charge  │  5   wading in deep water      │')
	print('\t└───────────────────────────────┼────────────────────────────────┤')
	print('\t                                │  6   foreign environment       │')
	print('\t                                ├────────────────────────────────┤')
	print('\t                                │  7   hindered/tangled/climbing │')
	print('\t                                ├────────────────────────────────┤')
	print('\t                                │  8   waiting                   │')
	print('\t                                └────────────────────────────────┘')
	x = input("\nEnter Mods:    ")

	mod = 0

	if '0' in x:
		mod += -2
	if '1' in x:
		mod += -1
	if '2' in x:
		mod += -2
	if '3' in x:
		mod += 2
	if '4' in x:
		mod += 2
	if '5' in x:
		mod += 4
	if '6' in x:
		mod += 6
	if '7' in x:
		mod += 3
	if '8' in x:
		mod += 1

	a = random.randint(1,10)
	o = a + mod
	print('\t╔═══════════════╗')
	print('\t║\t{}\t║\t RESULT'.format(o))
	print('\t╚═══════════════╝')
	print('\t      [ {} ]\t\t DICE ROLLS\n\t     mod: {}'.format((a),mod))
	xyz = input('press Enter to return')

# DAYLIGHT, SUNRISE, SUNSET
def daylight(day,climate):
	climates = ['arctic', 'subarctic', 'temperate', 'subtropical', 'tropical']
	c = climates.index(climate)

	daylightmap = [
	[7.5, 21.5, 23.5, 24, 24, 22, 17.5, 4.5, 1, 0, 0, 2.5], # arctic
	[11.5, 14.5, 17.5, 19.5, 18, 16, 13, 10, 7, 5.5, 5.5, 9], # subarctic
	[12, 13, 14.5, 15.5, 14.5, 14, 12.5, 11, 9.5, 9, 9.5, 10.5], # temperate
	[12, 12.5, 13, 13.5, 13.5, 13, 12, 11.5, 11, 10.5, 11, 11.5], # subtropical
	[12, 12.5, 12.5, 12.5, 12.5, 12.5, 12, 12, 11.5, 11.5, 11.5, 12] # tropical
	]

	# get the month from the day
	month = int(day)%360/30
	month = int(month)

	dawn = str(13 - daylightmap[c][month]/2 + 1)
	dusk = str(13 + daylightmap[c][month]/2 + 1 - 12)

	dawn = dawn.split('.')
	dusk = dusk.split('.')

	dawn[1] = float(dawn[1])/100
	dusk[1] = float(dusk[1])/100

	dawn = '{}h{}'.format(dawn[0],int(dawn[1]*60))
	dusk = '{}h{}'.format(dusk[0],int(dusk[1]*60))
	for i in range(0,4-len(dawn)):
		dawn += "0"
	for i in range(0,4-len(dusk)):
		dusk += "0"
	for i in range(0,5-len(dawn)):
		dawn += " "
	for i in range(0,5-len(dusk)):
		dusk += " "

	dl = daylightmap[c][month]

	return([dawn,dusk,str(dl)])

# Supply and Demand Adjustments
def market():
	# roll 3d6
	roll = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

	os.system('cls')
	print(' Modifiers')
	print('┌──────────────────────┬───────────────────┐')
	print('│ a : war              │ f : gov pressure  │')
	print('├──────────────────────┼───────────────────┤')
	print('│ b : surplus          │ g : thieves       │')
	print('├──────────────────────┼───────────────────┤')
	print('│ c : shortage         │ h : inflation     │')
	print('├──────────────────────┼───────────────────┤')
	print('│ d : merchant war     │ i : drought       │')
	print('├──────────────────────┼───────────────────┤')
	print('│ e : disaster, plague │ j : new region    │')
	print('└──────────────────────┴───────────────────┘')
	print('')
	mods = input('What modifiers?: ')

	output = ""
	if 'a' in mods:
		x = input('How many months has the war lasted?: ')
		roll += int(int(x)/2)
		output += "Services even more expensive than this.\n"
	if 'b' in mods:
		x = input('How many months has the surplus lasted?: ')
		roll -= int(int(x)/3)
	if 'c' in mods:
		x = input('How many months has the shortage lasted?: ')
		roll += int(int(x)/3)
	if 'd' in mods:
		x = input("How many weeks has the merhcant war lasted?: ")
		roll += int(x)
		output += 'This only applies to the goods of the merchants at war.\n'
	if 'e' in mods:
		roll -= 6
		output += 'But necessities are more expensive on average.\n'

	if 'f' in mods:
		x = input('taxing or subsidizing?: ')
		y = input('How many months has the {} lasted?: '.format(x))
		if x == 'taxing':
			roll += int(y)
		else:
			roll -= int(y)
	if 'g' in mods:
		x = input('How many months have the thieves been a problem?: ')
		roll += int(x)
		output += "There are also {} less merchants and {} less loads per month.\n".format(int(x),int(x)*2)
	if 'h' in mods:
		x = input('How much gold has adventurers been bringing back?: ')
		roll += int(int(x)/100_000)
	if 'i' in mods:
		x = input('How many months has the drought/famine lasted?: ')
		roll += int(int(x)/4)
		output += "This only applies to food, everything else is less expensive.\n"
	if 'j' in mods:
		x = input("How many months has it been since discovery?: ")
		z = 10 - int(x)
		if z < 0:
			z = 0
		roll += z

	if roll < 2:
		roll = 2
	if roll > 20:
		roll = 20
	adjustments = [0,0,25,30,40,50,60,70,80,90,100,110,120,130,140,150,160,180,200,300,400]
	sd = adjustments[roll]
	junk = 0.10 * sd
	bad = 0.25 * sd
	normal = sd
	good = (1 + random.randint(1,10)/10) * sd
	supreme = (random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + random.randint(1,10))/10 * sd
	masterpiece = sd * random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10 + random.randint(1,20)/10

	junk = str(int(junk))
	bad = str(int(bad))
	normal = str(int(normal))
	good = str(int(good))
	supreme = str(int(supreme))
	masterpiece = str(int(masterpiece))
	for i in range(0,5-len(junk)):
		junk += " "
	for i in range(0,5-len(bad)):
		bad += " "
	for i in range(0,5-len(normal)):
		normal += " "
	for i in range(0,5-len(good)):
		good += " "
	for i in range(0,5-len(supreme)):
		supreme += " "
	for i in range(0,5-len(masterpiece)):
		masterpiece += " "

	os.system('cls')
	print('┌─────────────┬────────┐')
	print('│        junk │ {}% │'.format(junk))
	print('│         bad │ {}% │'.format(bad))
	print('│             │        │')
	print('│      normal │ {}% │'.format(normal))
	print('│             │        │')
	print('│        good │ {}% │'.format(good))
	print('│     supreme │ {}% │'.format(supreme))
	print('│ masterpiece │ {}% │'.format(masterpiece	))
	print('└─────────────┴────────┘')
	print('')
	print(output)
	xyz = input("Press Enter to return ")

# Proficiencies
def profs():
	os.system('cls')
	print('                                           Proficiencies')
	print('===================================================================================================')
	print(' 1  Agriculture          20  Endurance             37  Mining                55  Survival')
	print(' 2  Ancient History      21  Engineering           38  Mountaineering        56  Swimming')
	print(' 3  Animal Handling      22  Etiquette             39  Musical Instrument')
	print(' 4  Animal Lore                                                              57  Tightrope Walking')
	print(' 5  Animal Training      23  Fire-building         40  Navigation            58  Tracking')
	print(' 6  Appraising           24  Fishing                                         59  Tumbling')
	print(' 7  Armorer              25  Forgery               41  Pottery')
	print(' 8  Artistic Ability                                                         60  Ventriloquism')
	print(' 9  Astrology            26  Gaming                42  Reading Lips')
	print('                         27  Gem Cutting           43  Reading/Writing       61  Weaponsmithing')
	print('10  Blacksmithing                                  44  Religion              62  Weather Sense')
	print('11  Blind-fighting       28  Healing               45  Riding, Airborne      63  Weaving')
	print('12  Bowyer/Fletcher      29  Heraldry              46  Riding, Land-Based')
	print('13  Brewing              30  Herbalism             47  Rope Use')
	print('                         31  Hunting               48  Running')
	print('14  Charioteering')
	print('15  Cobbling             32  Juggling              49  Seamanship')
	print('16  Cooking              33  Jumping               50  Seamstress/Tailor')
	print('                                                   51  Set Snares')
	print('17  Dancing              34  Languages, Ancient    52  Singing')
	print('18  Direction Sense      35  Languages, Modern     53  Spellcraft')
	print('19  Disguise             36  Local History         54  Stonemasonry')
	print('')
	p = input("what proficiency? ")
	with open('proficiencies/proficiencies.txt') as prof_file:
		prof_file = prof_file.readlines()
	p = prof_file[int(p)-1]
	p = p.split('\\n')
	step = 32
	for i in range(0,len(p),step):
		os.system('cls')
		a = i
		pp = p[a:a+step]
		for i in pp:
			print(i)
		input('\npress Enter to continue ')
	input('press Enter to continue ')




def main(f,d,wilderness,climate,terrain,season):
	x = f[d]
	display(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],\
		x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],\
		x[17],x[18],x[19],x[20],x[21],\
		wilderness,climate,terrain,season)

d = 0



# get the first run of things
#climate = input('What climate? ')
#terrain = input('What terrain? ')
#season = input('What season? ')

climate = 'temperate'
terrain = 'forest'
season = 'spring'

# the main loop
while True:

	wilderness = surroundingwilderness(climate,terrain,season)

	main(f,d,wilderness,climate,terrain,season)
	print('commands    d : go to a specific day    1 : add 1 day                     r : random day     m : morale check')
	print('            l : new location            s : change location parameters    p : show plants    i : initiative')
	print('           sd : market forces          pr : look up proficiency')
	print('')
	x = input("enter command: ")
	if x == "d":
		x = input("what day: ")
		d = int(x)
		doy = d%360
		if doy < 90:
			season = "spring"
		elif doy < 180:
			season = "summer"
		elif doy < 270:
			season = "fall"
		else:
			season = "winter"
	elif x == "pr":
		profs()
	elif x == "r":
		d = random.randint(0,len(f))
		doy = d%360
		if doy < 90:
			season = "spring"
		elif doy < 180:
			season = "summer"
		elif doy < 270:
			season = "fall"
		else:
			season = "winter"
	elif x == "l":
		wilderness = surroundingwilderness(climate, terrain, season)
	elif x == "s":
		climate = input('What climate? ')
		terrain = input('What terrain? ')
		season = input('What season? ')
		wilderness = surroundingwilderness(climate,terrain,season)
	elif x == "p":
		plants(climate, terrain, season)
	elif x == "i":
		initiative()
	elif x == "m":
		morale()
	elif x == "":
		d += 1
		doy = d%360
		if doy < 90:
			season = "spring"
		elif doy < 180:
			season = "summer"
		elif doy < 270:
			season = "fall"
		else:
			season = "winter"
	elif x == "sd":
		market()
	else:
		d += int(x)
		doy = d%360
		if doy < 90:
			season = "spring"
		elif doy < 180:
			season = "summer"
		elif doy < 270:
			season = "fall"
		else:
			season = "winter"
	print('\n\n')