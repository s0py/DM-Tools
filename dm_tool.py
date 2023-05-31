import random
import os

def read_players():
	pass

def save_players():
	pass

def read_food(food_file):
	food_file = './saves/{}_food.txt'.format(food_file)
	food_list = []
	with open(food_file) as food_file_lines:
		for line in food_file_lines.readlines():
			food_line = line.replace('\n','').replace("'","").split(', ')
			food_line[1] = int(food_line[1])
			food_line[2] = int(food_line[2])
			food_list.append(food_line)
		#print(food_list)
		#input('')
	return(food_list)

def save_food(food_list,save_name):
	with open('saves/{}_food.txt'.format(save_name),'w') as food_file:
		food_file.write('\n'.join(str(line).replace('[','').replace(']','') for line in food_list))

def read_config(config_file):
	with open('./saves/{}_config.txt'.format(config_file)) as config_file:
		lines = config_file.readlines()
		weather_file = lines[0].replace('\n','')
		climate = lines[1].replace('\n','')
		terrain = lines[2].replace('\n','')
		season = lines[3].replace('\n','')
		day = int(lines[4].replace('\n',''))
	return([weather_file,climate,terrain,season,day])

def save_config(weather_file, climate, terrain, season, day,save_name):
	# write what file is used for weather
	# write what climate and terrain are
	# write the date
	with open('saves/{}_config.txt'.format(save_name), "w") as config_file:
		config_file.write(weather_file)
		config_file.write('\n')
		config_file.write(climate)
		config_file.write('\n')
		config_file.write(terrain)
		config_file.write('\n')
		config_file.write(season)
		config_file.write('\n')
		config_file.write(str(day))


# ask for the file
os.system("mode con lines=36 cols=150")
os.system('cls')

print('Save Files')
save_files = os.listdir('./saves/')
print('')
for i in save_files:
	if '_config' in i:
		print("\t {}".format(i.replace('_config.txt',"")))
save = input('\nplease enter the name of the save\nor press Enter to start a new one: ')

if save == "":
	food_list = [
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""],
		["",1,0,""]
		]
	# each element of the food list is a list itself containing:
	# food name, food type, days old, condition
	print('Here are the weather files you can choose from:')
	weather_files = os.listdir('./weather/')
	print('')
	i_of_f = 0
	for i in weather_files:
		i_of_f += 1
		if i != "weather gen":
			print("\t{}  {}".format(i_of_f,i))
			if (i_of_f-1)%10 == 9:
				print('')
	temp = input("Please enter the file name: ")
	# if there is none specified use the default
	if temp == "":
		file = "weather/arctic_forest_weather_5year.csv"
	else:
		# see if it's just a number
		if temp in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]:
			temp = weather_files[int(temp)-1]
		# otherwise make sure that there is a .csv
		if ".csv" in temp:
			file = 'weather/{}'.format(temp)
		else:
			file = 'weather/{}.csv'.format(temp)

	climate = 'temperate'
	terrain = 'forest'
	season = 'spring'
	d = 0

else:
	file,climate,terrain,season,d = read_config(save)
	food_list = read_food(save)


with open(file) as f:
	f = f.readlines()
for i in range(0,len(f)):
	f[i] = f[i].replace("\n","")
	f[i] = f[i].split(",")
f.pop(0)

# def display(rain,wind_max,day,weekday,month,monthday,\
# 	 hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
# 	 wind_low,wind_missile,wind_melee,wind_move,viz_day,\
# 	 viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season):
def display(rain,wind_max,day,weekday,month,monthday,\
	hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
	wind_low,wind_missile,wind_melee,wind_move,viz_day,\
	viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season,food_list):
	
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

	# deal with the stupid way we are displaying the food
	fl1_n =  str(food_list[0][0])
	fl1_s =  str(food_list[0][-1])
	fl2_n =  str(food_list[1][0])
	fl2_s =  str(food_list[1][-1])
	fl3_n =  str(food_list[2][0])
	fl3_s =  str(food_list[2][-1])
	fl4_n =  str(food_list[3][0])
	fl4_s =  str(food_list[3][-1])
	fl5_n =  str(food_list[4][0])
	fl5_s =  str(food_list[4][-1])
	fl6_n =  str(food_list[5][0])
	fl6_s =  str(food_list[5][-1])
	fl7_n =  str(food_list[6][0])
	fl7_s =  str(food_list[6][-1])
	fl8_n =  str(food_list[7][0])
	fl8_s =  str(food_list[7][-1])
	fl9_n =  str(food_list[8][0])
	fl9_s =  str(food_list[8][-1])
	fl10_n = str(food_list[9][0])
	fl10_s = str(food_list[9][-1])
	fl11_n = str(food_list[10][0])
	fl11_s = str(food_list[10][-1])
	fl12_n = str(food_list[11][0])
	fl12_s = str(food_list[11][-1])

	for i in range(0,16-len(fl1_n)):
		fl1_n += " "
	for i in range(0,3-len(fl1_s)):
		fl1_s += " "
	for i in range(0,16-len(fl2_n)):
		fl2_n += " "
	for i in range(0,3-len(fl2_s)):
		fl2_s += " "
	for i in range(0,16-len(fl3_n)):
		fl3_n += " "
	for i in range(0,3-len(fl3_s)):
		fl3_s += " "
	for i in range(0,16-len(fl4_n)):
		fl4_n += " "
	for i in range(0,3-len(fl4_s)):
		fl4_s += " "
	for i in range(0,16-len(fl5_n)):
		fl5_n += " "
	for i in range(0,3-len(fl5_s)):
		fl5_s += " "
	for i in range(0,16-len(fl6_n)):
		fl6_n += " "
	for i in range(0,3-len(fl6_s)):
		fl6_s += " "
	for i in range(0,16-len(fl7_n)):
		fl7_n += " "
	for i in range(0,3-len(fl7_s)):
		fl7_s += " "
	for i in range(0,16-len(fl8_n)):
		fl8_n += " "
	for i in range(0,3-len(fl8_s)):
		fl8_s += " "
	for i in range(0,16-len(fl9_n)):
		fl9_n += " "
	for i in range(0,3-len(fl9_s)):
		fl9_s += " "
	for i in range(0,16-len(fl10_n)):
		fl10_n += " "
	for i in range(0,3-len(fl10_s)):
		fl10_s += " "
	for i in range(0,16-len(fl11_n)):
		fl11_n += " "
	for i in range(0,3-len(fl11_s)):
		fl11_s += " "
	for i in range(0,16-len(fl12_n)):
		fl12_n += " "
	for i in range(0,3-len(fl12_s)):
		fl12_s += " "


	os.system('cls')
	print('═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
	print('this program is reading from : {}'.format(file))
	print('')
	print('                                             Current Conditions')
	print('┌───────────────────────────┬───────────┐ ┌──────────────────────┐ ┌─────────────────────────────────┐ ┌─────────────────────────┐')	# 1
	print('│       weather   hum: {} │   hi   lo │ │         wind         │ │     surrounding wilderness      │ │          food           │'.format(humiditymod))	# 2
	print('├───────────────────────────┼───────────┤ ├──────────────────────┤ ├─────────────────────────────────┤ ├─────────────────────────┤')	# 3
	print('│ {} │ {} {} │ │          {} │ │ hunt                            │ │  1 {} {} │'.format(rain,eff_hi,eff_lo,wind_max,fl1_s,fl1_n))	# 4
	print('│ {} │ {} {} │ │ {} │ │ {} │ │  2 {} {} │'.format(spec,hi,lo,winddir,wilderness[0][1],fl2_s,fl2_n))	# 5
	print('└───────────────────────────┴───────────┘ │                      │ │                                 │ │  3 {} {} │'.format(fl3_s,fl3_n))	# 6
	print('            ┌───────────────────────────┐ │ missiles {} │ │ fish                            │ │  4 {} {} │'.format(wind_missile,fl4_s,fl4_n))	# 7
	print(' {} │ {} {}  (d {})│ │    melee {} │ │ {} │ │  5 {} {} │'.format(climate,monthday,month,day,wind_melee,wilderness[1][0],fl5_s,fl5_n))	# 8
	print(' {} ├───────────────────────────┤ │     move {} │ │ {} │ │  6 {} {} │'.format(terrain,wind_move,wilderness[1][1],fl6_s,fl6_n))	# 9
	print(' {} │            day {} │ └──────────────────────┘ │ {} │ │  7 {} {} │'.format(season,viz_day,wilderness[1][2],fl7_s,fl7_n))	# 10
	print('            │       twilight {} │ ┌──────────────────────┐ │ {} │ │  8 {} {} │'.format(viz_twi,wilderness[1][3],fl8_s,fl8_n))		# 11
	print(' dawn {} │      moonlight {} │ │     morale checks    │ │                                 │ │  9 {} {} │'.format(dawn,viz_moon,fl9_s,fl9_n))		# 12
	print(' dusk {} │           dark {} │ ├──────────────────────┤ │ forage                          │ │ 10 {} {} │'.format(dusk,viz_dark,fl10_s,fl10_n))		# 13
	print(' ({} h)   └───────────────────────────┘ │ surprised            │ │      found : {} │ │ 11 {} {} │'.format(dl,wilderness[2][1],fl11_s,fl11_n))		# 14
	print('           ┌────────────────────────────┐ │ superior force       │ │ prof found : {} │ │ 12 {} {} │'.format(wilderness[2][2],fl12_s,fl12_n))
	print('           │      water min (pints)     │ │ ally slain by magic  │ │    problem : {} │ └─────────────────────────┘'.format(wilderness[2][3]))
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

# tracking food
def add_food(food_list):
	task = input("add or remove a food?: ")
	if task == "add":
		index = int(input('what food slot?: '))
		food_name = input("food item: ")
		print('food types')
		print('1. green plant/grains')
		print('2. fruit or vegetable')
		print('3. cooked meat')
		print('4. raw meat')
		food_type = int(input("what type of food? (enter number): "))
		food_age = input("how many days old?: ")
		if food_age == "":
			food_age = 0
		food_age = int(food_age)
		food_list[index-1] = [food_name,food_type,food_age,""]
	if task == "remove":
		food = int(input('what food item? (enter number): '))
		if food > 12:
			food = 12
		if food < 1:
			food = 1
		food_list[food-1] = ['',0,0,'']

	return(food_list)

# wilderness[11] is the eff_hi of the day
def update_food(food_list,temp):
	# how many days before a check is needed
	checkmap = [
	[0,6,4,2,1], # green plants
	[0,5,3,2,1], # fruits and vegetables
	[0,3,2,1,1], # cooked meat
	[0,2,1,1,1]  # raw meat
	]
	# percent chance of spoilage
	spoilmap = [
	[0,20,30,40,50],
	[0,30,40,50,60],
	[0,20,50,60,80],
	[0,50,70,80,90]
	]
	# turn the temp into an index
	if temp < 31:
		temp = 0
	elif temp in range(31,51):
		temp = 1
	elif temp in range(51,71):
		temp = 2
	elif temp in range(71,91):
		temp = 3
	elif temp > 90:
		temp = 4
	# one spoil check and the food is tainted
	# two and the food is obviously entirely spoiled
	for item in food_list:
		item[2] += 1
		# get the type and age
		food_type = item[1]-1
		food_age = item[2]
		# check to see if it's past the check time
		if food_age >= checkmap[food_type][temp]:
			# check to see if you advance the spoilage
			if random.randint(0,99) < spoilmap[food_type][temp]:
				print('rolled less than spoil chance')
				if item[3] == "" and item[0] != "":
					item[3] = "(T)"
				elif item[3] == "(T)":
					item[3] = "(S)"
	return(food_list)


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
		
		huntdist = "{} size, {} creatures @ {} yards".format(a[x-1],b,c)

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
	step = 31
	b = int(len(p)/step) + 1
	page = 1
	for i in range(0,len(p),step):
		os.system('cls')
		print('page {} of {}'.format(page,b))
		print('')
		a = i
		pp = p[a:a+step]
		for i in pp:
			print("\t{}".format(i))
		print('\npage {} of {}'.format(page,b))
		page += 1
		input('press Enter to continue ')
	input('press Enter to return ')

# combat modifiers
def combat():
	os.system('cls')
	print('')
	print('                          Combat Modifiers')
	print('┌───────────────────────────────┬──────────────────────────────────┐')
	print('│ Attacker on high ground :  +1 │     Defender stunned/prone :  +4 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│      Defender invisible :  -4 │         Defender surprised :  +1 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│    Defender off-balance :  +2 │   Missile fire, long range :  -5 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│  Defender sleeping/held :  XX │ Missile fire, medium range :  -2 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│       Defender kneeling :  +1 │       Defender laying down :  +4 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│        Defender sitting :  +2 │    Attacker using off-hand :  -2 │')
	print('└───────────────────────────────┼──────────────────────────────────┤')
	print(' XX - automatically hits. if    │                Rear attack :  -2 │')
	print('      not in combat, defender   └──────────────────────────────────┘')
	print('      is slain automatically.')
	input('\npress Enter to return ')




def main(f,d,wilderness,climate,terrain,season,food_list):
	x = f[d]
	display(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],\
		x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],\
		x[17],x[18],x[19],x[20],x[21],\
		wilderness,climate,terrain,season,food_list)

def update_season(d):
	doy = d%360
	if doy < 90:
		season = "spring"
	elif doy < 180:
		season = "summer"
	elif doy < 270:
		season = "fall"
	else:
		season = "winter"
	return(season)

prev_day = -1
# the main loop
while True:

	# get the wilderness info
	wilderness = surroundingwilderness(climate,terrain,season)
	# update all the food
	if prev_day != -1 and d != 0:
		for i in range(prev_day,d):
			temp = f[i][11]
			food_list = update_food(food_list,int(temp))
	prev_day = d

	main(f,d,wilderness,climate,terrain,season,food_list)
	print('commands    d : go to a specific day    1 : add 1 day                     f : add/remove food    m : morale check')
	print('            l : new location            s : change location parameters    p : show plants        i : initiative')
	print('           sd : market forces          pr : look up proficiency           c : combat mods       sa : save')
	print('')
	x = input("enter command: ")
	if x == "d":
		x = input("what day: ")
		prev_day = d
		d = int(x)
		season = update_season(d)
	elif x == "x":
		print(food_list)
		input('')
	elif x == "f":
		food_list = add_food(food_list)
	elif x == "sa":
		# ask for the information
		save_name = input('Please name your save: ')
		save_config(file,climate,terrain,season,d,save_name)
		save_food(food_list,save_name)
	elif x == "c":
		combat()
	elif x == "pr":
		profs()
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
		prev_day = d
		d += 1
		season = update_season(d)
	elif x == "sd":
		market()
	else:
		prev_day = d
		d += int(x)
		season = update_season(d)
	print('\n\n')