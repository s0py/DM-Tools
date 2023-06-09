from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.columns import Columns

import random
from os import system, listdir

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
	return((weather_file,climate,terrain,season,day))

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
system("mode con lines=36 cols=150")
system('cls')

print('Save Files')
save_files = listdir('./saves/')
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
	weather_files = listdir('./weather/')
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
		if temp in ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"):
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
	checkmap = (
	(0,6,4,2,1), # green plants
	(0,5,3,2,1), # fruits and vegetables
	(0,3,2,1,1), # cooked meat
	(0,2,1,1,1)  # raw meat
	)
	# percent chance of spoilage
	spoilmap = (
	(0,20,30,40,50),
	(0,30,40,50,60),
	(0,20,50,60,80),
	(0,50,70,80,90)
	)
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

def poison():
	system('cls')
	print('\t')
	print('\t                Poisons')
	print('\tClass     Method      Onset         Strength')
	print('\t--------------------------------------------')
	print('\t    A     Injected    10-30 mins    15/0')
	print('\t    B     Injected     2-12 mins    20/1d3')
	print('\t    C     Injected     2-5 mins     25/2d4')
	print('\t    D     Injected     1-2 mins     30/2d6')
	print('\t')
	print('\t    E     Injected    Immediate     Death/20')
	print('\t    F     Injected    Immediate     Death/0')
	print('\t    G     Ingested    2-12 hours    20/10')
	print('\t    H     Ingested    1-4 hours     20/10')
	print('\t')
	print('\t    I     Ingested    2-12 mins     30/15')
	print('\t    J     Ingested    1-4 mins      Death/20')
	print('\t    K      Contact    2-8 mins      5/0')
	print('\t    L      Contact    2-8 mins      10/0')
	print('\t')
	print('\t    M      Contact    1-4 mins      20/5')
	print('\t    N      Contact      1 mins      Death/25')
	print('\t    O     Injected    2-24 mins     Paralytic')
	print('\t    P     Injected    1-3 hours     Debilitative')
	input('\npress enter to continue')

def treasure_gen():
	# this program generates treasure in accordance with the tables
	o = ""
	gem = 0
	art = 0
	magic_item = False
	
	def d(x, y, z):
		output = "\n> "
		x = x.split("d")
		t = 0
		a = int(x[0])
		b = int(x[1])
		for i in range(0,a):
			t += random.randint(1,b)
		output += str(t*y)
		output += ' ' + str(z)
		return(output)
	
	def dd(x, y, z):
		output = ""
		x = x.split("d")
		t = 0
		a = int(x[0])
		b = int(x[1])
		for i in range(0,a):
			t += random.randint(1,b)
		output += str(t*y)
		output += ' ' + str(z)
		return(output)
	
	def p():
		return(random.random()*100)
	
	
	code = input("what treasure letter? (a - z): ")
	
	
	########################################################
	#    Loot
	########################################################
	o += "\n == Coins == "
	if code == "a":
		# copper
		if p() < 25:
			o += d('1d3', 1000, 'cp')
		# silver
		if p() < 30:
			o += d('2d10', 100, 'sp')
		# gold
		if p() < 40:
			o += d('1d6', 1000, 'gp')
		# platinum
		if p() < 35:
			o += d('3d6', 100, 'pp')
		# gems
		if p() < 60:
			gem = random.randint(1,4) * 10
		# art objects
		if p() < 50:
			art = random.randint(1,6) + random.randint(1,6)
		# magic items
		if p() < 30:
			magic_item	= True
	if code == "b":
		# copper
		if p() < 50:
			o += d('1d6', 1000, 'cp')
		if p() < 25:
			o += d('1d3', 1000, 'sp')
		if p() < 25:
			o += d('2d10', 100, 'gp')
		if p() < 25:
			o += d('1d10', 100, 'pp')
		if p() < 30:
			gem = random.randint(1,8)
		if p() < 20:
			art = random.randint(1,4)
		if p() < 10:
			magic_item = True
	if code == "c":
		if p() < 20:
			o += d('1d10', 1000, 'cp')
		if p() < 30:
			o += d('1d6', 1000, 'sp')
		if p() < 10:
			o += d('1d6', 100, 'pp')
		if p() < 25:
			gem = random.randint(1,6)
		if p() < 20:
			art = random.randint(1,3)
		if p() < 10:
			magic_item = True
	if code == "d":
		if p() < 10:
			o += d('1d6', 1000, 'cp')
		if p() < 15:
			o += d('1d10', 1000, 'sp')
		if p() < 50:
			o += d('1d3', 1000, 'gp')
		if p() < 15:
			o += d('1d6', 100, 'pp')
		if p() < 30:
			gem = random.randint(1,10)
		if p() < 25:
			art = random.radint(1,6)
		if p() < 15:
			magic_item = True
	if code == 'e':
		if p() < 5:
			o+= d('1d6', 1000, 'cp')
		if p() < 25:
			o += d('1d10', 1000, 'sp')
		if p() < 25:
			o += d('1d4', 100, 'gp')
		if p() < 25:
			o += d('3d6', 100, 'pp')
		if p() < 15:
			gem = random.randint(1,12)
		if p() < 10:
			art = random.randint(1,6)
		if p() < 25:
			magic_item	= True
	if code == 'f':
		if p() < 10:
			o += d('3d6', 1000, 'sp')
		if p() < 40:
			o += d('1d6', 1000, 'gp')
		if p() < 15:
			o += d('1d4', 1000, 'pp')
		if p() < 20:
			gem = random.randint(1,10) + random.randint(1,10)
		if p() < 10:
			art = random.randint(1,8)
		if p() < 30:
			magic_item = True
	if code == 'g':
		if p() < 50:
			o += d('2d10', 1000, 'gp')
		if p() < 50:
			o += d('1d10', 1000, 'pp')
		if p() < 30:
			gem = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
		if p() < 10:
			art = random.randint(1,6)
		if p() < 30:
			magic_item = True
	if code == 'h':
		if p() < 25:
			o += d('3d6', 1000, 'cp')
		if p() < 40:
			o += d('2d10', 1000, 'sp')
		if p() < 55:
			o += d('2d10', 1000, 'gp')
		if p() < 40:
			o += d('1d8', 1000, 'pp')
		if p() < 50:
			gem = random.randint(1,10) + random.randint(1,10) + random.randint(1,10)
		if p() < 50:
			art = random.randint(1,10) + random.randint(1,10)
		if p() < 15:
			magic_item = True
	if code == 'i':
		if p() < 30:
			o += d('1d6', 100, 'pp')
		if p() < 55:
			gem = random.randint(1,6) + random.randint(1,6)
		if p() < 50:
			art = random.randint(1,4) + random.randint(1,4)
		if p() < 15:
			magic_item = True
	if code == 'j':
		o += d('3d8', 1, 'cp')
	if code == 'k':
		o += d('3d6',1,'sp')
	if code == 'l':
		o += d('2d6', 1, 'pp')
	if code == 'm':
		o += d('2d4',1,'gp')
	if code == 'n':
		o += d('1d6',1,'pp')
	if code == 'o':
		o += d('1d4',10,'cp')
		o += d('1d3',10,'sp')
	if code == 'p':
		o += d('1d6',10,'sp')
		o += d('1d20',1,'pp')
	if code == 'q':
		gem = random.randint(1,4)
	if code == 'r':
		o += d('2d10',1,'gp')
		o += d('1d6',10,'pp')
		gem = random.randint(1,4) + random.randint(1,4)
		art = random.randint(1,3)
	if code == 's':
		magic_item = True
	if code == 't':
		magic_item = True
	if code == 'u':
		if p() < 90:
			gem = random.randint(1,8) + random.randint(1,8)
		if p() < 80:
			art = random.randint(1,6)
		if p() < 70:
			magic_item = True
	if code == 'v':
		magic_item = True
	if code == 'w':
		o += d('5d6',1,'gp')
		o += d('1d8',1,'pp')
		if p() < 60:
			gem = random.randint(1,8) + random.randint(1,8)
		if p() < 50:
			art = random.randint(1,8)
		if p() < 60:
			magic_item = True
	if code == 'x':
		magic_item = True
	if code == 'y':
		o == d('2d6',100,'gp')
	if code == 'z':
		o += d('1d3',100,'cp')
		o += d('1d4',100,'sp')
		o += d('1d6',100,'gp')
		o += d('1d4',100,'pp')
		if p() < 55:
			gem = random.randint(1,6)
		if p() < 50:
			art = random.randint(1,6) + random.randint(1,6)
		if p() < 50:
			magic_item = True
	
	
	########################################################
	#    Gems
	########################################################
	if gem > 0:
		o += "\n\n == Gems == "
		sp = ""
		gc1 = 0
		gc2 = 0
		gc3 = 0
		gc4 = 0
		gc5 = 0
		gc6 = 0
		gn1 = ""
		gn2 = ""
		gn3 = ""
		gn4 = ""
		gn5 = ""
		gn6 = ""
		ornamental = ("Azurite: Opaque, mottled deep blue", "Banded Agate: Brown, blue, red, and white stripes", "Blue Quartz: Transparent pale blue", "Eye Agate: Gray, white, brown, blue, and green circles", "Hematite: Gray-black", "Lapis Lazuli: Light or dark blue with yellow flecks", "Malachite: Striated light and dark green", "Moss Agate: Pink, yellow-white with gray-green moss-like markings", "Obsidian: Jet black", "Rhodochrosite: Light pink", "Tiger Eye Agate: Rich golden brown with dark striping", "Turquoise: Aqua with darker mottling")
		semiprecious = ("Bloodstone: Dark gray with red flecks","Carnelian: Orange to red-brown","Chalcedony: White","Chrysoprase: Translucent apple to emerald green","Citrine: Pale yellow brown","Jasper: Blue, black to brown","Moonstone: White with pale blue hue","Onyx: Black, white, or bands of both","Rock Crystal: Clear, transparent","Sardonyx: Bands of red and white","Smoky Quartz: light gray, yellow, brown or blue","Star Rose Quartz: Smoky rose with white star center","Zircon: Clear pale aqua")
		fnacy = ("Amber: Transparent golden", "Alexan")
		fancy_precious = ("Amber: Transparent golden","Alexandrite: Dark green","Amethyst: Purple crystal","Aquamarine: pale blue green","Chrysoberyl: green or yellow green","Coral: Pink to crimson","Garnet: Deep red to violet crystal","Jade: Light to dark green or white","Jet: Deep black","Pearl: Pure white, rose, to black","Peridot: Olive green","Spinel: Red, red-brown, green, or deep blue","Topaz: Golden yellow","Tourmaline: Pale green, blue, brown, or red")
		gems_jewels = ("Black Opal: Dark green with black mottling and golden flecks","Black Sapphire: Rich black with highlights","Diamond: Clear blue-white, rich blue, yellow, or pink","Emerald: Brilliant green","Fire Opal: Fiery red","Jacinth: Fiery orange","Opal: Pale blue with green and gold mottling","Oriental Amethyst: Deep purple","Oriental Emerald: Bright green","Oriental Topaz: Fiery yellow","Ruby: Clear to deep crimson red","Sapphire: Clear to medium blue","Star Ruby: Translucent ruby with white star highlights","Star Sapphire: Translucent blue with white star highlights")
	
		# pick one of each category
		gn1 = random.choice(ornamental)
		gn2 = random.choice(semiprecious)
		gn3 = random.choice(fancy_precious)
		gn4 = gn3
		gn5 = random.choice(gems_jewels)
		gn6 = gn5
	
		for g in range(0,gem):
			# find out how many of each gem
			rg = random.randint(1,100)
			if rg in range(1,26):
				gc1 += 1
			elif rg in range(26,51):
				gc2 += 1
			elif rg in range(51,71):
				gc3 += 1
			elif rg in range(71,91):
				gc4 += 1
			elif rg in range(91-100):
				gc5 += 1
			else:
				gc6 +=1
			# fill it all out
	
		for i in range(0,gc1):
			sp = ""
			u = ""
			base = 10
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn1
			o += " ({} gp)".format(int(base))
			o += u
			o += sp
		o += "\n-"
	
		for i in range(0,gc2):
			sp = ""
			u = ""
			base = 50
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn2
			o += " ({} gp)".format(int(base))
			o += u
			o += sp
		o += "\n -"
	
		for i in range(0,gc3):
			sp = ""
			u = ""
			base = 100
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn3
			o += " ({} gp)".format(int(base))
			o += u
			o += sp
		o += "\n -"
	
		for i in range(0,gc4):
			sp = ""
			u = ""
			base = 500
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn4
			o += " ({} gp) [Large]".format(int(base))
			o += u
			o += sp
		o += "\n -"
	
		for i in range(0,gc5):
			sp = ""
			u = ""
			base = 1000
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn5
			o += " ({} gp)".format(int(base))
			o += u
			o += sp
		o += "\n -"
	
		for i in range(0,gc6):
			sp = ""
			u = ""
			base = 5000
			uncut = False
			special = False
			if random.randint(0,9) < 1:
				uncut = True
			if uncut == True:
				base *= 0.90
				u = " [Uncut]"
	
			if random.randint(0,9) < 1:
				special = True
			if special == True:
				gvariation = random.randint(1,6)
				sp = ""
				if gvariation == 1:
					base *= 3
					sp = " [Perfect]"
				if gvariation == 2:
					base *= 2
					sp = " [Above Average]"
				if gvariation == 3:
					base *= (1 + random.randint(1,6)*.1)
					sp = " [Above Average]"
				if gvariation == 4:
					base *= (1 - random.randint(1,4)*.1)
					sp = " [Below Average]"
				if gvariation == 5:
					base *= 0.5
					sp = " [Below Average]"
				if gvariation == 6:
					base *= 0.33
					sp = " [Horrid]"
	
			o += "\n> {}. ".format(i + 1)
			o += gn6
			o += " ({} gp) [Large]".format(int(base))
			o += u
			o += sp
	
	########################################################
	#    Art Objects
	########################################################
	if art > 0:
		o += "\n\n == Art Objects == "
	
	for a in range(0,art):
		aroll = random.randint(1,100)
		base = 0
		aout = "\n> "
	
		if aroll in range(0,11):
			value = d('1d10',10,'gp')
		if aroll in range(11,26):
			value = d('3d6',10,'gp')
		if aroll in range(26,41):
			value = d('1d6',100,'gp')
		if aroll in range(41,51):
			value = d('1d10',100,'gp')
		if aroll in range(51,61):
			value = d('2d6',100,'gp')
		if aroll in range(61,71):
			value = d('3d6',100,'gp')
		if aroll in range(71,81):
			value = d('4d6',100,'gp')
		if aroll in range(81,86):
			value = d('5d6',100,'gp')
		if aroll in range(86,91):
			value = d('1d4',1000,'gp')
		if aroll in range(91,96):
			value = d('1d6',1000,'gp')
		if aroll in range(96,100):
			value = d('2d4',1000,'gp')
		if aroll == 100:
			value = d('2d6',1000,'gp')
	
		objetsdart = ("A beautiful elven vase that is slightly cracked. The painting around the outside of the vase depicts an elven god planting the world’s very first tree.", "Artwork of a battle showing the local lords fighting off an attack, painted by a long dead artist. The painting is set in a lovely gold leaf frame.", "A child’s painting framed beautifully. The art itself is fairly lacking but the frame is worth a decent amount, even more to someone who appreciates the juxtaposition of incredibly classy and messy.", "A jade tea set for two, stored on a lovely wooden tray.", "A large stone that (magically/naturally) glows. It is crafted into a statuette of a celestial being. The stone itself is worth little but the craftsmanship is very fine.", "A baby’s blanket made of the finest cloth. It is kept in a mothballed container for years. It smells faintly of mint, as if someone meant to store it for a very long time.", "A model of the solar system you reside in. It is made entirely out of brass with some of the labels faded over time. It could possibly be sold to a place of knowledge for a slightly higher price.", "A finely made flask and flask sheath. The flask is slightly dirty on the inside but with some running water and time, it will reveal a noble’s crest on the side immediately, skyrocketing the value.", "A deed to a very small portion of land that now resides in the very middle of a noble’s house. The city will buy it off of you for a good price.", "A golden likeness of the hand of a legendary female warlord, sitting atop a small pedestal bearing her name (Alanna the Fearless). The hand is able to hold a sword that is made to her specific specifications, all others simply fall out.", "A jade carving of a dog etched with its eulogy.", "Two delicate links of silver chain around a demon statuette of rare wood. Of particular interest to that demon’s cult.", "Seven beautifully etched bells in descending sizes, each made of silver and each with its own tone. Ringing one makes you slightly sleepy, others fill you with talkative urge or a powerful sense of unease.", "A handful of jasper puzzle pieces speckled with flecks of semiprecious stone (citrine, amethyst, garnet, etc.) that assemble themselves into the 2-D likeness of the last animal you pointed at.", "A painting of middling skill drawn by a local lord who has recently passed. “He was a bastard when he was alive. but an endearing one now he’s dead!”", "A painting of exquisite skill drawn by a discredited masterandom. “Hm… probably a fake. I’ll give you 100 gold, consider yourself lucky.”", "A palm-sized bronze automaton of a goose that lays a copper egg. Its eyes are rubies. Feed it copper coins and it produces more copper eggs.", "A small sapphire hairpin carved into the shape of an ocean wave.", "A volume of poetry by the late great bard _______.", "A volume of painstakingly illuminated holy scripture – bookmarked to some of the racier passages.", "A beautifully crafted but unbalanced and obviously impractical weapon. Is it a long-handled sword? A short-handled spear with a long blade? A throwing javelin with a 10-foot range?", "A silver and brass mirror with lewd designs hidden around the frame.", "The gaudy holy symbol of a cult to the defunct goddess of wealth.", "A small notebook with the random musings of ‘The Authorandom.’ Many of them pertain about the nature of the world, time, space and the future. Oddly no one has noticed that all the predictions in said notebook have come true.", "A crudely made painting of a king smiling. The painting itself is nothing special. What is however special is the painter but being one of his worse works it gets a rather low price.", "The (nonmagical) axe of Gunthar the Brave, a hero that is very well known and celebrated in his hometown, but not very well known elsewhere.", "A fancy belt buckle (broken beyond repair) from a legendary wizard hero, engraved with his initials.", "A set of candlesticks that on casual glance look extremely expensive which, upon very close examination, turn out to be made of brass instead of gold and with glass instead of gemstones.", "An exquisite scrimshaw design of dueling dragons made from a harpy claw.", "A chunk of metal that, when inspected, is just 100 gp melted and welded togetherandom.", "A clay pot full of a rare and valuable spice.", "A ridiculously unusable gold-plated fantasy sword.", "A canvas swatch full of lines and streaks of colors, all of which methods of color reproduction are lost to time.", "A round table with engraved magic circle and runes that casts a random Prestidigitation effect every day on a fixed lantern in the middle of the table.", "A blue-blade sword within a black leather sheath trimmed with silver leaves. It can be pulled out, but not drawn all the way out.", "A 2-foot golden statue of the deity Waukeen. Waukeen is seated on a chair made of coins.", "The beautifully carved silver lance tip of Sir Thais. It had tipped his ceremonial lance, which was all he had when the [insert current npc group the PCs just fought] brazenly ambushed the king’s parade a few months ago. The tip broke off after being plunged into the shoulder of [a bad guy] and was recovered by [bad guy minions]. Sadly, being ceremonial, the designs are intricate but not really effective for a lance tip, nearly blunt.", "A silver ring with a small piece of jet set in it.", "Boots that magically stay warm and dry, no matter what they’ve been through.", "A filigree gold goblet once owned by a prince.", "An amphora of ancient Fey wine (still good, and very tasty).", "A crown of wyvern fangs set in silverandom.", "A white cape with red embroidery. As you spill blood on the cape, the embroidery grows.", "A silver lined demon skull drinking cup.", "A gold brooch inlaid with jet and garnet.", "Huge ornately carved mahogany doors. Very heavy.", "A gilded and illuminated manuscript.", "A small box inlaid with mother of pearl.", "A matching pair of platinum rings. Each with a large pearl inset. They are worth 50gp each; or 100 gp for the set.", "The keystone of the entrance arch from a legendary temple destroyed in an ancient warandom. (50lb) – priceless to the right collectorandom.", "A 12x12ft, intricately patterned, thick, silk carpet. (200lb)", "An elven viol decorated with silver vines.", "A black onyx scepter with a head of a crow carved in the handle.", "A tapestry depicting the rise and fall of a recently conquered nearby city-state.", "A ceramic jug with glyphs of people teaching the spell ‘create food and water’. Can be used by wizards to copy into spell book.", "A see-through glass sword. The blade is made out of a clear blue glass while the handle is tinted blue.", "Ghostly and spectral remains that have been encased in a Crystal Ball. The ball glows faintly and has a swirling mist effect inside.", "A sheathe for a short sword long since forgotten. It is made with purple velvet wrapped owlbear leather, capped at the end by electrum. The inside has been smoothed considerably and lined with gelatinous cube remains. The effect of this is realized when drawing the sword, the sheathe generates zero sound whatsoeverandom. There is a carved wooden replica of the sword inside the sheathe, and all are contained within a see-through glass case wherein the sheathe lays horizontally.", "A headframe for a bed made with black ash logs. There are carved pictures of ravens decorating the headboard, and gold has been pressed into the carvings.", "A small gem encrusted crown, too small for most races, the crown is unique in that it has horsehair attached, allowing the crown to be worn as a wig.", "Iron ball and chain, there are carefully chiseled etchings in the chain and around the ball in dwarvish. If read, the etchings reveal a song about a criminal held in confinement for killing a noble, but her jailhouse was besieged by bandits for a yearandom. After the first verse, the faint chiseled etchings become deeper and clearer, telling of the dwarf’s temporary release and subsequent victory in combat of the besiegers alongside her jailers. The third and final verse is carved faintly and carefully again, detailing the dwarf continuing her life sentence until her death.", "An ivory tusk the length of an arm but carved with scenes from a battle long ago.", "A polished brass and copper clockwork toy of a small cottage, a farmer and their animals that moves when wound. The farmer chases a toy chicken with an axe.", "A scrimshaw pipe. When puffed on small skeletal animal smoke shapes rise out.", "A white porcelain chamber pot, the much-maligned last work of a great artist who went mad. The pot has the signature of the artist scrawled on it in a shaky hand.", "A painting that was started but not finished that depicts a beautiful landscape. It was started by a famous painter but unfortunately, he died halfway through finishing it. Parts of it are still sketched while others are fully painted.", "A tiny sundial made from a single piece of platinum.", "This ornate oak chair is both artsy AND functional. Sculpted by talented elven Craftsman as a wealthy dining set but have been split up due to warandom. Each chair depicts a different scene in a major war that happened thousands of years ago.", "A small, ornate hand-mirror, with decorative trim and a quote running along the edges that reads ‘Beauty is Diligence in Physical Form’.", "a painting with a mage shouting spells, it is clearly readable out of his mouth, but the letters become denser and denser until it’s only black paint.", "A portrait that makes a 3d bust illusion of a designated person. Requires a simple ritual to ‘take the picture’.", "A mirror that makes you look more attractive via illusion magic.", "A vase made from beautiful stone, carved with celestial figures around it, some marble inlays", "A silver circlet with a glowing stone in it, it can be used to cast light once per day", "An abstract art piece, not of any notable artist, but painted with specks of stones with permanent and colorful illumination.", "An ornate mantle clock that rings the hour with twelve separate melodies.", "A boldly colored quartz the size of a pigeon’s egg, etched and painted in such a way that when it is placed to one’s eye in the light, they see a clever but naughty image of a beautiful person in the nude.", "A wood bound codex filled illuminated with several hundred pages of highly colorful and anatomically difficult descriptions of sexual positions. The codex is sealed with a small brass chain. The text of the manuscript is in a language that is not common.", "A disk of clay with extremely fine etchings of semi-concentric lines that seem to spiral outwards from the center in tight, semi random wiggly spirals. It has been broken into three shards.", "A hat-stand made with ornate knobs of polished brass on the ends of the hooks. The knobs are animal heads in fine detail.", "A desktop ornament made of pink clear glass in the shape of a pig with a bright red glass apple in its mouth. When the pig is rubbed, it makes a magical oink noise.", "An ornate, decorative inkpot and penknife made of rare animal horn.", "A wire basket handled rapier of ornate design, with a fake ruby made of glass mounted in the pommel. The rapier is mounted to be a trophy on a wall. A small plaque reads, ‘Wrath’.", "A large globe showing the known world and a nested set of platonic solids, all made of brass. The entire contraption is over a meter across.", "A palm sized gelatinous cube containing a finely crafted model ship. The cube has been permanently suspended in animation with magic and is non-threatening.", "A painting of a flail snail enhanced by magic to project faint rainbow light from the shell of the flail snail.", "a handcrafted dreamcatcher adorned with werewolf teeth", "The mask of a cloud giant. The mask is pearl white and has light pink stripes.", "A sentient, immobile, carved basalt statue of a jellyfish, summoned to godhood by a cult of Koa-Toa", "Silver Body chains, worn by a high priestess Yuan-Ti.", "A mind flayers brain kept inside of a glass containerandom.", "A perfectly preserved molt of a Yuan-Ti Abomination. The molt is displayed on a large wooden platform.", "A necklace with a large pearl eye, around the eye are ten smaller pearl eyes branching off of the central eye. The necklace is gold and fashioned to depict a beholderandom.", "A small wood totem carved to resemble a werewolf, stolen from a cult of Malarandom.", "A clock in the image of an owlbear’s face. It is of masterwork gnomish quality. Every hour the owlbear opens its mouth and a -hoot hoot- sound emanates from the clock. At nighttime the eyes of the owlbear glow blood red.", "A gnomish tinkered hummingbird that fly’s in place for eternity.", "A palm sized jade turtle. While visibly impressive, most appraisers know it is of sub-par craftsmanship.", "A glass display with the first 100 gold coins minted by a nearby dwarven civilization.", "A display of a stone giants stone club. far too heavy to wield by medium sized creatures.", "A grey ooze that has been polymorphed into a throw rug. The ooze is unable to move across the floor on its own, however is constantly moving ‘within’ itself, giving the appearance of a swirling void.", "A palm sized carved stone replica of the Tomb of Horrors.", "A single Coatl feather, on a palm leaf.", "A candle made of red wax, in the image of a fire salamander", "A candle holder fashioned to resemble a fire mephit holding the candle. The candle holder is made of silverandom.", "The crown of a lizard king. The crown is made of gold and has images of lizardfolk fighting various fey creatures for control of a swamp.", "A perfectly preserved bone skull of a Sahuagin, on a corral wall mount", "The wrappings of a mummy inside a locked trunk.", "A small living carnivorous plant, inside of a notably larger iron cage.", "A carved golden sun, meant to mounted on a wall", "A stone tiled gameboard. the gameboard has stone figurines of adventurers fighting goblins in a dungeon.", "A painting of a ship sailing away from Waterdeep bay.", "A carved tusk of an unknown monster, depicting druids in the middle of a ritual", "An ornate, smooth orb of hardened tree sap (mixed with lavender dye.) It has the appearance of a round translucent ball (the size of a tennis ball in real life) with a dark purple hue and is often mistaken for an old family heirloom. Perhaps an Eboron spell wright believes it is her great grandmother’s spell casting focus, passed down for generations, or is a rather loud-mouthed, malicious constable found in his office every morning adoring his magnificent paper weight with an unusual amount of quiet glee?", "A singular wooden box, with 1-year worth of every spice in the world.", "A non-magical stone ‘official’ seal carved of three birds in flight with a blank spot where the buyer’s official crest can be added.", "Six ornately decorated candles with religious symbolism, and tapers (for lighting), in a small, smoked boxwood case of fine craftsmanship, with space for a seventh candle.", "A finely tanned, soft leather pouch filled with thirty-six small, polished hematite tiles about 2 cm across, inscribed with non-magical glyphs on both sides. Some of the tiles have different glyphs on opposing sides. The pouch has a leather drawstring.", "A birch and mahogany game-board approximately 30 centimeters across. The squares of the board are arrayed in a 9×9 pattern. A small set of two matching birch tables only 10 centimeters high accompany the board.", "A brass and glass hand-mirror with an intricate wirework for the handle. The wirework is of a bird in a cage.", "A polished brass telescoping spyglass, compass, octant, and slide rule set with precisely engraved markings and extreme precision. It comes in a velvet lined wooden case that has been treated with beeswax.", "A small chest for storing jewels in but made completely without nails. The outside of the chest has been lacquered red and inlaid with some very fine parquetry of a fruiting tree.", "A gilded oil lamp with ornate scrollwork cutouts of a warrior, and an evil sorcerer, meant to cast shadows on the wall in their shape.", "A fine glass lensed magnifying glass tied by a red silk ribbon to a codex filled with hundreds of pages of detailed illumination regarding the natural world.")
	
		aout += random.choice(objetsdart)
		value = value.replace('\n> ','')
		aout += " ({})".format(value)
	
		o += aout
	
	
	########################################################
	#    Magic Items
	########################################################
	
	###############
	# Potion Picker
	def potions():
		potion = "\n> Potion: "
		d6 = random.randint(1,3)
		p1 = ("Animal Control (250 gp)", "Clairaudience (250 gp)", "Clairvoyance (300 gp)", "Climbing (300 gp)", "Delusion", "Delusion", "Diminution (300 gp)", "Dragon Control (700 gp)", "Elixir of Health (350 gp)", "Elixir of Madness", "Elixir of Madness", "Elixir of Youth (500 gp)", "ESP (500 gp)", "Extra-healing (400 gp)", "Extra-healing (400 gp)", "Fire Breath (400 gp)", "Fire Resistance (250 gp)", "Flying (500 gp)", "Gaseous Form (300 gp)")
		p2 = ("Giant Control (600 gp)","Giant Strength Warrior (550 gp)","Growth (250 gp)","Healing (200 gp)","Healing (200 gp)","Heroism Warrior (300 gp)","Human Control (500 gp)","Invisibility (250 gp)","Invulnerability Warrior (350 gp)","Levitation (250 gp)","Longevity (500 gp)","Oil of Acid Resistance (500 gp)","Oil of Disenchantment (750 gp)","Oil of Elemental Invulnerability (500 gp)","Oil of Etherealness (600 gp)","Oil of Fiery Burning (500 gp)","Oil of Fumbling","Oil of Impact (750 gp)","Oil of Slipperiness (400 gp)")
		p3 = ("Oil of Timelessness (500 gp)","Philter of Glibness (500 gp)","Phliter of Love (200 gp)","Phliter of Persuasiveness (400 gp)","Phliter of Stammering and Stuttering","Plant Control (250 gp)","Poison","Poison","Polymorph Self (200 gp)","Rainbow Hues (200 gp)","Speed (200 gp)","Super-heroism Warrior (450 gp)","Super-heroism Warrior (450 gp)","Weet Water (200 gp)","Treasure Finding (600 gp)","Undead Control (700 gp)","Ventriloquism (200 gp)","Vitality (300 gp)","Water Breathing (400 gp)")
		if d6 == 1:
			potion += random.choice(p1)
		if d6 == 2:
			potion += random.choice(p2)
		if d6 == 3:
			potion += random.choice(p3)
		return(potion)
	
	###########
	# Scroll Picker
	def scrolls():
		sout = "\n> Scroll: "
		level = ""
		#             1 2 3 4 5 6 7 8 9 a b c d e f g h i j
		num_spells = (1,1,1,1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7)
		wll = (1,1,1,1,1,2,1,2,1,2,1,1,1,1,1,3,1,2,4)
		wlu = (4,4,4,5,5,9,4,9,4,9,6,8,6,8,6,8,8,9,9)
		pll = (1,1,1,1,1,2,1,2,1,2,1,1,1,1,1,3,1,2,4)
		plu = (4,4,4,6,6,7,4,7,4,7,6,6,6,6,6,6,8,7,7)
	
		d6 = random.randint(1,3)
		if d6 == 1 or d6 == 2:
			d20 = random.randint(1,19) - 1
			for i in range(0,num_spells[d20]):
				priest = False
				if random.random() > 0.7:
					priest = True
				if priest == False:
					level = random.randint(wll[d20], wlu[d20])
					sout += "Level {} Wizard Spell".format(level)
				if priest == True:
					level = random.randint(pll[d20], plu[d20])
					sout += "Level {} Priest Spell".format(level)
				sout += ", "
	
		if d6 == 3:
			d20 = random.randint(0,18)
			non_spell_scrolls = ("Map", \
			"Protection from Acid (2500 xp)", \
			"Protection from Cold (2000 xp)", \
			"Protection from Dragon Breath (2000 xp)", \
			"Protection from Electricity (1500 xp)", \
			"Protection from Elementals (1500 xp)", \
			"Protection from Elementals (1500 xp)", \
			"Protection from Fire (2000 xp)", \
			"Protection from Gas (2000 xp)", \
			"Protection from Lycanthropes (1000 xp)", \
			"Protection from Lycanthropes (1000 xp)", \
			"Protection from Magic (1500 xp)", \
			"Protection from Petrification (2000 xp)", \
			"Protection from Plants (1000 xp)", \
			"Protection from Poison (1000 xp)", \
			"Protection from Possession (2000 xp)", \
			"Protection from Undead (1500 xp)", \
			"Protection from Water (1500 xp)", \
			"Cursed")
			sout += non_spell_scrolls[d20]
	
		return(sout)
	
	##############
	# Ring Picker
	def rings():
		rout = "\n> Ring of "
		d20 = random.randint(0,18)
		rings_low = ("Animal Friendship (1000 xp)",\
					"Blinking (1000 xp)",\
					"Chameleon Power (1000 xp)",\
					"Clumsiness",\
					"Contrariness",\
					"Delusion",\
					"Delusion",\
					"Djinni Summoning (limited charges) (3000 xp)",\
					"Elemental Command (5000 xp)",\
					"Feather Falling (1000 xp)",\
					"Fire Resistance (1000 xp)",\
					"Free Action (1000 xp)", \
					"Human Influence (2000 xp)", \
					"Invisibility (1500 xp)", \
					"Jumping (1000 xp)",\
					"Jumping (1000 xp)",\
					"Mammal Control (limited charges) (1000 xp)",\
					"Protection (1000xp * level of protection)")
	
		rings_high = ("Protection (1,000 xp * level of protection xp)", \
		"Protection (1,000 xp * level of protection xp)", \
		"the Ram (750 xp)", \
		"Regeneration (5,000 xp)", \
		"Shocking Grasp (1,000 xp)", \
		"Shooting Stars (3,000 xp)", \
		"Spell Storing (2,500 xp)", \
		"Spell Turning (2,000 xp)", \
		"Sustenance (500 xp)", \
		"Swimming (1,000 xp)", \
		"Telekinesis (limited charges) (2,000 xp)", \
		"Truth (1,000 xp)", \
		"Warmth (1,000 xp)", \
		"Water Walking (1,000 xp)", \
		"Weakness ", \
		"Multiple Wishes (limited charges) (5,000 xp)", \
		"3 Wishes (limited charges) (3,000 xp)", \
		"Wizardry (limted charges) Wizard  (4,000 xp)", \
		"X-Ray Vision (4,000 xp)")
	
		d3 = random.randint(1,3)
		if d3 == 1 or d3 == 2:
			rout += random.choice(rings_low)
		elif d3 == 3:
			rout += random.choice(rings_high)
		
		return(rout)
	
	#################
	# Rod Picker
	def rods():
		rout = "\n> Rod of "
		rods = ("Absorption Priest, Wizard (7,500 xp)", \
		"Absorption Priest, Wizard (7,500 xp)", \
		"Alertness (7,000 xp)", \
		"Alertness (7,000 xp)", \
		"Beguiling Priest, Wizard, Rogue (5,000 xp)", \
		"Cancellation (10,000 xp)", \
		"Cancellation (10,000 xp)", \
		"Flailing (2,000 xp)", \
		"Lordly Might (Warrior) (6,000 xp)", \
		"Passage (5,000 xp)", \
		"Resurrection (Priest) (10,000 xp)", \
		"Rulership (8,000 xp)", \
		"Security (3,000 xp)", \
		"Security (3,000 xp)", \
		"Smiting Priest, Wizard (4,000 xp)", \
		"Smiting Priest, Wizard (4,000 xp)", \
		"Splendor (2,500 xp)", \
		"Terror (3,000 xp)", \
		"Terror (3,000 xp)")
	
		rout += random.choice(rods)
		return(rout)
	
	#################
	# Staff Picker
	def staffs():
		stout = "\n> Staff of "
		staffs = ("Mace (1500 xp)",\
			"Mace (1500 xp)",\
			"Command Priest Wizard (5000 xp)",\
			"Curing Priest (6000 xp)",\
			"Curing Priest (6000 xp)",\
			"Magi Wizard (15000 xp)",\
			"Power Wizard (12000 xp)",\
			"Serpent Priest (7000 xp)",\
			"Slinging Priest (2000 xp)",\
			"Slinging Priest (2000 xp)",\
			"Spear (1000 xp per level)",\
			"Spear (1000 xp per level)",\
			"Striking Priest Wizard (6000 xp)",\
			"Striking Priest Wizard (6000 xp)",\
			"Swarming Insects Priest Wizard (100 xp per charge)",\
			"Thunder & Lightning (8000 xp)",\
			"Withering (8000 xp)",\
			"Withering (8000 xp)",\
			"Woodlands Druid (8000 xp)")
		stout += random.choice(staffs)
		return(stout)		
			
	################
	# Wand Picker
	def wands():
		wout = "\n> Wand of "
		wands = ("Conjuration (Wizard) (7,000 xp)", \
					"Earth and Stone (1,000 xp)", \
					"Enemy Detection (2,000 xp)", \
					"Fear (Priest, Wizard) (3,000 xp)", \
					"Fire (Wizard) (4,500 xp)", \
					"Flame Extinguishing (1,500 xp)", \
					"Frost (Wizard) (6,000 xp)", \
					"Illumination (2,000 xp)", \
					"Illusion (Wizard) (3,000 xp)", \
					"Lightning (Wizard) (4,000 xp)", \
					"Magic Detection (2,500 xp)", \
					"Magic Missiles (4,000 xp)", \
					"Metal and Mineral Detection (1,500 xp)", \
					"Negation (3,500 xp)", \
					"Paralyzation (Wizard) (3,500 xp)", \
					"Polymorphing (Wizard) (3,500 xp)", \
					"Secret Door and Trap Location (5,000 xp)", \
					"Size Alteration (3,000 xp)", \
					"Wonder (6,000 xp)")
		wout += random.choice(wands)
		return(wout)
	
	################
	# Misc Books and Tomes Picker
	def booksandtomes():
		bout = "\n> "
		l = ("Boccob’s Blessed Book (Wizard) (4,500 xp)", \
					"Boccob’s Blessed Book (Wizard) (4,500 xp)", \
					"Boccob’s Blessed Book (Wizard) (4,500 xp)", \
					"Book of Exalted Deeds (Priest) (8,000 xp)", \
					"Book of Infinite Spells (9,000 xp)", \
					"Book of Vile Darkness (Priest) (8,000 xp)", \
					"Libram of Gainful Conjuration (Wizard) (8,000 xp)", \
					"Libram of Ineffable Damnation (Wizard) (8,000 xp)", \
					"Libram of Silver Magic (Wizard) (8,000 xp)", \
					"Manual of Bodily Health (5,000 xp)", \
					"Manual of Gainful Exercise (5,000 xp)", \
					"Manual of Golems (Priest, Wizard) (3,000 xp)", \
					"Manual of Puissant Skill at Arms (Warrior) (8,000 xp)", \
					"Manual of Quickness in Action (5,000 xp)", \
					"Manual of Stealthy Pilferin (Rogue) (8,000 xp)", \
					"Tome of Clear Thought (8,000 xp)", \
					"Tome of Leadership and Influence (7,500 xp)", \
					"Tome of Understanding (8,000 xp)", \
					"Vacuous Grimoire")
		bout += random.choice(l)
		return(bout)
	
	################
	# Misc Jewels and Jewelry Picker
	def jewelry():
		jout = "\n> "
		l1 = ("Amulet of Inescapable Location", \
					"Amulet of Life Protection (5,000 xp)", \
					"Amulet of the Planes (6,000 xp)", \
					"Amulet of Proof Against Detection and Location (4,000 xp)", \
					"Amulet Versus Undead (200 xp per level)", \
					"Beads of Force (200 xp ea.)", \
					"Brooch of Shielding (1,000 xp)", \
					"Gem of Brightness (2,000 xp)", \
					"Gem of Insight (3,000 xp)", \
					"Gem of Seeing (2,000 xp)", \
					"Jewel of Attacks", \
					"Jewel of Flawlessness", \
					"Medallion of ESP (2,000 xp)", \
					"Medallion of Thought Projection", \
					"Necklace of Adaptation (1,000 xp)", \
					"Necklace of Missiles (100 xp per die of damage)", \
					"Necklace of Missiles (100 xp per die of damage)", \
					"Necklace of Prayer Beads (Priest) (500 xp per bead)", \
					"Necklace of Strangulation")
		l2 = ("Pearl of Power (Wizard) (200 xp per level)", \
					"Pearl of the Sirines (900 xp)", \
					"Pearl of Wisdom (Priest) (500 xp)", \
					"Periapt of Foul Rotting", \
					"Periapt of Health (1,000 xp)", \
					"Periapt of Proof Against Poison (1,500 xp)", \
					"Periapt of Wound Closure (1,000 xp)", \
					"Phylactery of Faithfulness (Priest) (1,000 xp)", \
					"Phylactery of Long Years (Priest) (3,000 xp)", \
					"Phylactery of Monstrous Attention (Priest)", \
					"Scarab of Death", \
					"Scarab of Enraging Enemies (1,000 xp)", \
					"Scarab of Insanity (1,500 xp)", \
					"Scarab of Protection (2,500 xp)", \
					"Scarab Versus Golems", \
					"Talisman of Pure Good (Priest) (3,500 xp)", \
					"Talisman of the Sphere (Wizard) (100 xp)", \
					"Talisman of Ultimate Evil (Priest) (3,500 xp)", \
					"Talisman of Zagy (1,000 xp)")
	
		if random.randint(1,2) == 1:
			jout += random.choice(l1)
		else:
			jout += random.choice(l2)
	
		return(jout)
	
	################
	# Misc Cloaks and Robes Picker
	def cloaks():
		rout = "\n> "
		l = ("Cloak of Arachnida (3,000 xp)", \
					"Cloak of Displacement (3,000 xp)", \
					"Cloak of Elvenkind (1,000 xp)", \
					"Cloak of Elvenkind (1,000 xp)", \
					"Cloak of Poisonousness", \
					"Cloak of Protection (1,000 xp per point)", \
					"Cloak of Protection (1,000 xp per point)", \
					"Cloak of the Bat (1,500 xp)", \
					"Cloak of the Manta Ray (2,000 xp)", \
					"Robe of the Archmagi (Wizard) (6,000 xp)", \
					"Robe of Blending (3,500 xp)", \
					"Robe of Eyes (Wizard) (4,500 xp)", \
					"Robe of Powerlessness (Wizard)", \
					"Robe of Scintillating Colors (Priest, Wizard) (2,750 xp)", \
					"Robe of Stars (Wizard) (4,000 xp)", \
					"Robe of Useful Items (Wizard) (1,500 xp)", \
					"Robe of Useful Items (Wizard) (1,500 xp)", \
					"Robe of Vermin (Wizard)")
		rout += random.choice(l)
		return(rout)
	
	################
	# Misc Boots and Gloves Picker
	def boots():
		bout = "\n> "
		l = ("Boots of Dancing", \
					"Boots of Elvenkind (1,000 xp)", \
					"Boots of Levitation (2,000 xp)", \
					"Boots of Speed (2,500 xp)", \
					"Boots of Striding and Springing (2,500 xp)", \
					"Boots of the North (1,500 xp)", \
					"Boots of Varied Tracks (1,500 xp)", \
					"Boots, Winged (2,000 xp)", \
					"Bracers of Archery (Warrior) (1,000 xp)", \
					"Bracers of Brachiation (1,000 xp)", \
					"Bracers of Defense (500 xp per AC less than 10)", \
					"Bracers of Defense (500 xp per AC less than 10)", \
					"Bracers of Defenselessness", \
					"Gauntlets of Dexterity (1,000 xp)", \
					"Gauntets of Fumbling", \
					"Gauntlets of Ogre Power (Priest, Rogue, Warrior) (1,000 xp)", \
					"Gauntlets of Swimming and Climbing (Priest, Rogue, Warrior) (1,000 xp)", \
					"Gloves of Missile Snaring (1,500 xp)", \
					"Slippers of Spider Climbing (1,000 xp)")
		bout += random.choice(l)
		return(bout)
	
	################
	# Misc Girdles and Helms Picker
	def girdles():
		out = "\n> "
		l =("Girdle of Dwarvenkind (3,500 xp)", \
					"Girdle of Dwarvenkind (3,500 xp)", \
					"Girdle of Dwarvenkind (3,500 xp)", \
					"Girdle of Femininity/Masculinity", \
					"Girdle of Giant Strength (Priest, Rogue, Warrior) (2,000 xp)", \
					"Girdle of Giant Strength (Priest, Rogue, Warrior) (2,000 xp)", \
					"Girdle of Many Pouches (1,000 xp)", \
					"Girdle of Many Pouches (1,000 xp)", \
					"Hat of Disguise (1,000 xp)", \
					"Hat of Stupidity", \
					"Helm of Brilliance (2,500 xp)", \
					"Helm of Comprehending", \
					"Helm of Comprehending", \
					"Languages and Reading", \
					"Magic (1,000 xp)", \
					"Helm of Opposite Alignment", \
					"Helm of Telepathy (3,000 xp)", \
					"Helm of Teleportation (2,500 xp)", \
					"Helm of Underwater Action (1,000 xp)", \
					"Helm of Underwater Action (1,000 xp)")
		out += random.choice(l)
		return(out)
	
	################
	# Misc Bags and Bottles Picker
	def bags():
		out = "\n> "
		l = ("Alchemy Jug (3,000 xp)", \
					"Bag of Beans (1,000 xp)", \
					"Bag of Devouring", \
					"Bag of Holding (5,000 xp)", \
					"Bag of Holding (5,000 xp)", \
					"Bag of Holding (5,000 xp)", \
					"Bag of Holding (5,000 xp)", \
					"Bag of Transmuting", \
					"Bag of Tricks (2,500 xp)", \
					"Beaker of Plentiful Potions (1,500 xp)", \
					"Bucknard’s Everfull Purse", \
					"Decanter of Endless Water (1,000 xp)", \
					"Efreeti Bottle (9,000 xp)", \
					"Eversmoking Bottle (500 xp)", \
					"Flask of Curses", \
					"Heward’s Handy Haversack (3,000 xp)", \
					"Iron Flask", \
					"Portable Hole (5,000 xp)", \
					"Pouch of Accessibility 1,500")
		out += random.choice(l)
		return(out)
	
	################
	# Misc Dusts and Stones Picker
	def dusts():
		out = "\n> "
		l = ("Candle of Invocation (Priest) (1000 xp)", \
					"Dust of Appearance (1000 xp)", \
					"Dust of Disappearance (2000 xp)", \
					"Dust of Dryness (1000 xp)", \
					"Dust of Illusion (1000 xp)", \
					"Dust of Tracelessness (500 xp)", \
					"Dust of Sneezing and Choking", \
					"Incense of Meditation (Priest) (500 xp)", \
					"Incense of Obsession (Priest)", \
					"Ioun Stones (300 xp per stone)", \
					"Keoghtom’s Ointment 500", \
					"Nolzur’s Marvelous Pigments 500 xp per stone", \
					"Philosopher’s Stone (1000 xp)", \
					"Smoke Powder**", \
					"Sovereign Glue (1000 xp)", \
					"Stone of Controlling Earth Elementals (1500 xp)", \
					"Stone of Good Luck (Luckstone) (3000 xp)", \
					"Stone of Weight (Loadstone)", \
					"Universal Solvent (1000 xp)")
		out += random.choice(l)
		return(out)
	
	################
	# Misc Household Items and Tools Picker
	def tools():
		out = "\n> "
		l = ("Brazier Commanding Fire Elementals (Wizard) (4000 xp)", \
					"Brazier of Sleep Smoke (Wizard)", \
					"Broom of Animated Attack", \
					"Broom of Flying (2000 xp)", \
					"Carpet of Flying (7500 xp)", \
					"Mattock of the Titans (Warrior) (3500 xp)", \
					"Maul of the Titans (Warrior) (4000 xp)", \
					"Mirror of Life Trapping (Wizard) (2500 xp)", \
					"Mirror of Mental Prowess (5000 xp)", \
					"Mirror of Opposition", \
					"Murlynd’s Spoon (750 xp)", \
					"Rope of Climbing (1000 xp)", \
					"Rope of Climbing (1000 xp)", \
					"Rope of Constriction", \
					"Rope of Entanglement (1500 xp)", \
					"Rug of Smothering", \
					"Rug of Welcome (Wizard) (6500 xp)", \
					"Saw of Mighty Cutting (Warrior) (2000 xp)", \
					"Spade of Colossal Excavation (Warrior) (1000 xp)")
		out += random.choice(l)
		return(out)
	
	################
	# Misc Musical Instruments Picker
	def instruements():
		out = "\n> "
		l = ("Chime of Interruption (2000 xp)", \
					"Chime of Opening (3500 xp)", \
					"Chime of Hunger", \
					"Drums of Deafening", \
					"Drums of Panic (6500 xp)", \
					"Harp of Charming (5000 xp)", \
					"Harp of Discord", \
					"Horn of Blasting (1000 xp)", \
					"Horn of Bubbles", \
					"Horn of Collapsing (1500 xp)", \
					"Horn of Fog (400 xp)", \
					"Horn of Goodness (Evil) (750 xp)", \
					"Horn of the Tritons (Priest, Warrior) (2000 xp)", \
					"Horn of Valhalla (1000 xp)", \
					"Lyre of Building (5000 xp)", \
					"Pipes of Haunting (400 xp)", \
					"Pipes of Pain", \
					"Pipes of Sounding (1000 xp)", \
					"Pipes of the Sewers (2000 xp)")
		out += random.choice(l)
		return(out)
	
	
	################
	# Misc Weird Stuff Picker
	def weird():
		out = "\n> "
		l = ("Apparatus of Kwalish (8000 xp)", \
					"Folding Boat (10000 xp)", \
					"Folding Boat (10000 xp)", \
					"Bowl Commanding Water Elementals (Wizard) (4000 xp)", \
					"Bowl of Watery Death (Wizard)", \
					"Censer Controlling Air Elementals (Wizard) (4000 xp)", \
					"Censer of Summoning Hostile Air Elementals (Wizard)", \
					"Crystal Ball (Wizard) (1000 xp)", \
					"Crystal Ball (Wizard) (1000 xp)", \
					"Crystal Hypnosis Ball (Wizard)", \
					"Cube of Force (3000 xp)", \
					"Cube of Frost Resistance (2000 xp)", \
					"Cube of Frost Resistance (2000 xp)", \
					"Cubic Gate (5000 xp)", \
					"Daern’s Instant Fortress (7000 xp)", \
					"Deck of Illusions (1500 xp)", \
					"Deck of Many Things", \
					"Eyes of Charming (Wizard) (4000 xp)", \
					"Eyes of Minute Seeing (2000 xp)", \
					"Eyes of Petrification", \
					"Eyes of the Eagle (3500 xp)", \
					"Figurine of Wondrous Power (100 xp per HD of figurine)", \
					"Figurine of Wondrous Power (100 xp per HD of figurine)", \
					"Horseshoes of a Zephyr (1500 xp)", \
					"Horseshoes of Speed (2000 xp)", \
					"Horseshoes of Speed (2000 xp)", \
					"Iron Bands of Bilarro (750 xp)", \
					"Lens of Detection (250 xp)", \
					"Quaal’s Feather Token (1000 xp)", \
					"Quiver of Ehlonna (1500 xp)", \
					"Quiver of Ehlonna (1500 xp)", \
					"Sheet of Smallness (1500 xp)", \
					"Sphere of Annihilation (4000 xp)", \
					"Stone Horse (2000 xp)", \
					"Well of Many Worlds (6000 xp)", \
					"Wind Fan (500 xp)", \
					"Wind Fan (500 xp)", \
					"Wings of Flying (750 xp)")
		out += random.choice(l)
		return(out)
	
	################
	# Armor Picker
	def armors():
		out = "\n> Armor: "
		mod = ""
	
		# get type of armor
		armors = ('Banded mail', \
						  "Brigandine", \
						  "Chain mail", \
						  "Chain mail", \
						  "Chain mail", \
						  "Field plate", \
						  "Full plate", \
						  "Leather", \
						  "Plate mail", \
						  "Plate mail", \
						  "Plate mail", \
						  "Plate mail", \
						  "Ring mail", \
						  "Scale mail", \
						  "Shield small", \
						  "Shield buckler", \
						  "Shield medium", \
						  "Shield large", \
						  "Splint mail", \
						  "Studded leather", \
						  "Special")
		a = random.choice(armors)
		
		# determine if special
		special_armors = ("Armor of Command (+1000 xp)", "Armor of Blending (+500 xp)", "Armor of Missile Attraction", "Armor of Rage", "Elven Chain Mail (+1000 xp)", "Plat Mail of Etherealness (5000 xp)", "Plate Mail of Fear (4000 xp)", "Plate Mail of Vulnerability", "Shield large, -1 AC, -4 AC vs missiles (400 xp)", "Shield +1 AC, Missile Attractor")
		if a == "Special":
			a = random.choice(special_armors)
			out += a
		
		# determine mod
		else:
			d20 = random.randint(0,19)
			xps = (0, 0, 500, 500, 500, 500, 500, 500, 500, 500, 500, 1000, 1000, 1000, 1000, 1500, 1500, 1500, 2000, 2000, 3000)
			mods =(1, 1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   -2,   -2,   -2,   -2,   -3,   -3,   -3,   -4,   -4,   -5)
	
			mod = random.choice(mods)
			xp = random.choice(xps)
			out += a
			out += " {} mod".format(str(mod))
			out += " ({} xp)".format(str(xp))
		return(out)
	
	
	################
	# Weapon Picker
	def weapons():
		out = "\n> Weapon: "
		w = ""
		mod = ""
		d20 = random.randint(1,40)
		special = False
		if d20 == 1:
			w += dd('4d6',1,"Arrows")
		elif d20 == 2:
			w += dd('3d6',1,"Arrows")
		elif d20 == 3:
			w += dd('2d6',1,'Arrows')
		elif d20 == 4 or d20 == 5:
			w += "Axe"
		elif d20 == 6:
			w += "Battle axe"
		elif d20 == 7:
			w += dd('2d10',1,"Bolts")
		elif d20 == 8:
			w += dd('2d6',1,'Bolts')
		elif d20 == 9:
			w += dd('3d4',1,'Sling bullets')
		elif d20 == 10 or d20 == 11 or d20 == 12:
			w += "Dagger"
		elif d20 == 13:
			w += dd('3d4',1,'Darts')
		elif d20 == 14:
			w += "Flail"
		elif d20 == 15:
			w += dd('1d2',1,'Javelins')
		elif d20 == 16:
			w += "Knife"
		elif d20 == 17:
			w += "Lance"
		elif d20 == 18 or d20 == 19:
			w += "Mace"
		elif d20 == 20 or d20 == 40:
			special = True
		elif d20 == 21:
			w += "Military pick"
		elif d20 == 22:
			w += "Morning Star"
		elif d20 == 23:
			w += "Pole Arm"
		elif d20 == 24 or d20 == 25:
			w += "Scimitar"
		elif d20 == 26 or d20 == 27 or d20 == 28:
			w += "Spear"
		elif d20 in range(29,38):
			w += "Sword"
		elif d20 == 38:
			w += "Trident"
		elif d20 == 39:
			w += "Warhammer"
	
		if special == True:
			d10 = random.randint(1,10)
			sw1 = ("Arrow of Direction (2500 xp)", \
								"Arrow of Slaying (250 xp)", \
								"Axe +2, Throwing (750 xp)", \
								"Axe of Hurling", \
								"Bow +1 (500 xp)", \
								"Bow +1 (500 xp)", \
								"Crossbow of Accuracy, +3 (2000 xp)", \
								"Crossbow of Distance (1500 xp)", \
								"Crossbow of Speed (1500 xp)", \
								"Dagger +1, +2 vs. Tiny or Small creatures (300 xp)", \
								"Dagger +1, +2 vs. Tiny or Small creatures (300 xp)", \
								"Dagger +2, +3 vs. larger than man–sized creatures (300 xp)", \
								"Dagger +2, +3 vs. larger than man–sized creatures (300 xp)", \
								"Dagger +2, Longtooth (300 xp)", \
								"Dagger of Throwing", \
								"Dagger of Venom (350 xp)", \
								"Dart of Homing (450 xp)", \
								"Hammer +3, Dwarven Thrower (1500 xp)", \
								"Hammer of Thunderbolts (2500 xp)")
			sw2 = ("Hornblade", \
								"Javelin of Lightning (250 xp)", \
								"Javelin of Piercing (250 xp)", \
								"Knife Buckle (150 xp)", \
								"Knife Buckle (150 xp)", \
								"Mace of Disruption (2000 xp)", \
								"Mace of Disruption (2000 xp)", \
								"Net of Entrapment (1000 xp)", \
								"Net of Snaring (1000 xp)", \
								"Quarterstaff Magical (500 xp)", \
								"Quarterstaff Magical (500 xp)", \
								"Scimitar of Speed", \
								"Sling of Seeking +2 (70 xp)", \
								"Sling of Seeking +2 (70 xp)", \
								"Spear Cursed Backbiter", \
								"Trident of Fish Command (50 xp)", \
								"Trident of Submission (150 xp)", \
								"Trident of Warning (100 xp)", \
								"Trident of Yearning")
			sw3 = ("Sun Blade (3000 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +2 vs. magic-using & enchanted creatures (600 xp)", \
								"Sword +1, +3 vs. lycanthropes & shape-changers (700 xp)", \
								"Sword +1, +3 vs. lycanthropes & shape-changers (700 xp)", \
								"Sword +1, +3 vs. lycanthropes & shape-changers (700 xp)", \
								"Sword +1, +3 vs. regenerating creatures (800 xp)", \
								"Sword +1, +3 vs. regenerating creatures (800 xp)", \
								"Sword +1, +4 vs. reptiles (800 xp)", \
								"Sword +1, Cursed", \
								"Sword +1, Cursed", \
								"Sword +1, Flame Tongue (900 xp)", \
								"Sword +1, Luck Blade (1000 xp)", \
								"Sword +2, Dragon Slayer (900 xp)", \
								"Sword +2, Giant Slayer (900 xp)")
			sw4 = ("Sword +2 Nine Lives Stealer (1600 xp)", \
								"Sword +3 Frost Brand (1600 xp)", \
								"Sword +3 Frost Brand (1600 xp)", \
								"Sword +4 Defender (3000 xp)", \
								"Sword +5 Defender (3600 xp)", \
								"Sword +5 Holy Avenger (4000 xp)", \
								"Sword –2 Cursed", \
								"Sword –2 Cursed", \
								"Sword of Dancing (4400 xp)", \
								"Sword of Life Stealing (5000 xp)", \
								"Sword of Sharpness (7000 xp)", \
								"Sword of the Planes (2000 xp)", \
								"Sword of Wounding (4400 xp)", \
								"Sword Cursed Berserking", \
								"Sword Cursed Berserking", \
								"Sword Cursed Berserking", \
								"Sword Short Quickness (+2) (1000 xp)", \
								"Sword Short Quickness (+2) (1000 xp)", \
								"Sword Vorpal Weapon (10000 xp)")
			if d10 == 1 or d10 == 2 or d10 == 3:
				out += random.choice(sw1)
			elif d10 == 4 or d10 == 5 or d10 == 6:
				out += random.choice(sw2)
			elif d10 == 7 or d10 == 8 or d10 == 9:
				out += random.choice(sw3)
			else:
				out += random.choice(sw4)
	
		else:
			d20 = random.randint(1,20)
			if w == "Sword":
				if d20 == 1 or d20 == 2:
					mod = "-1"
				elif d20 in range(3,11):
					mod = "+1 (400 xp)"
				elif d20 in range(11,15):
					mod = "+2 (800 xp)"
				elif d20 in range(15,18):
					mod = "+3 (1400 xp)"
				elif d20 == 18 or d20 == 19:
					mod = "+4 (2000 xp)"
				elif d20 == 20:
					mod = "+5 (3000 xp)"
			else:
				if d20 == 1 or d20 == 2:
					mod = "-1"
				elif d20 in range(3,11):
					mod = "+1 (500 xp)"
				elif d20 in range(11,15):
					mod = "+1 (500 xp)"
				elif d20 in range(15,18):
					mod = "+2 (1000 xp)"
				elif d20 == 18 or d20 == 19:
					mod = "+2 (1000 xp)"
				elif d20 == 20:
					mod = "+3 (2000 xp)"
			out += "{} {}".format(w, mod)
		return(out)
	
	################
	# Magic Items
	def magic(n):
		if n in range(1,21):
			a = str(potions())
		elif n in range(21,36):
			a = str(scrolls())
		elif n in range(36,41):
			a = str(rings())
		elif n == 41:
			a = str(rods())
		elif n == 42:
			a = str(staffs())
		elif n in range(43,46):
			a = str(wands())
		elif n == 46:
			a = str(booksandtomes())
		elif n==47 or n==48:
			a = str(jewelry())
		elif n==49 or n==50:
			a = str(cloaks())
		elif n==51 or n==52:
			a = str(boots())
		elif n==53:
			a = str(girdles())
		elif n==54 or n==55:
			a = str(bags())
		elif n==56:
			a = str(dusts())
		elif n==57:
			a = str(tools())
		elif n==58:
			a = str(instruements())
		elif n==59 or n==60:
			a = str(weird())
		elif n in range(61,76):
			a = str(armors())
		elif n in range(76,101):
			a = str(weapons())
		return(a)
	
	
	###############
	# Picking the Items
	if magic_item == True:
		o += "\n\n == Magic Items == "
		if code == "a":
			# any 3
			for i in range(0,3):
				o += magic(random.randint(1,100))
		if code == "b":
			# armor weapon
			r = random.randint(61,100)
			o += magic(r)
		if code == "c":
			# any 2
			for i in range(0,2):
				o += magic(random.randint(1,100))
		if code == "d":
			# any 1 + 1 potion
			o += magic(random.randint(1,100))
			o += magic(random.randint(1,20))
		if code == "e":
			# any 3 + 1 scroll
			for i in range(0,3):
				o += magic(random.randint(1,100))
			o += magic(random.randint(21,35))
		if code == "f":
			# any 5 except weapons
			for i in range(0,5):
				o += magic(random.randint(1,75))
		if code == "g":
			# any 5
			for i in range(0,5):
				o += magic(random.randint(1,100))
		if code == "h":
			# any 6
			for i in range(0,6):
				o += magic(random.randint(1,100))
		if code == "i":
			# any 1
			o += magic(random.randint(1,100))
		if code == "s":
			# 1-8 potions
			r = random.randint(1,8)
			for i in range(0,r):
				o += magic(random.randint(1,20))
		if code == "t":
			# 1d4 scrolls
			r = random.randint(1,4)
			for i in range(0,r):
				o += magic(random.randint(21,35))
		if code == "u":
			# any 1
			o += magic(random.randint(1,100))
		if code == "v":
			# any 2
			for i in range(0,2):
				o += magic(random.randint(1,100))
		if code == "w":
			# any 2
			for i in range(0,2):
				o += magic(random.randint(1,100))
		if code == "x":
			# any 2 potions
			o += magic(random.randint(1,20))
			o += magic(random.randint(1,20))
		if code == "z":
			# any 3
			for i in range(0,3):
				o += magic(random.randint(1,100))
	
	system('cls')
	print(" == Loot == ")
	print(o)
	print("\n")
	input('press Enter to continue ')

# hunting
def hunting(climate, terrain, season):
	# map -> biome -> terrain -> season
	huntmap = (
		((5,5,10,5),(5,5,10,10),(5,5,10,10),(5,5,5,5),(5,10,10,5),(5,10,10,5),(5,10,10,5)), # arctic
		((5,10,10,5),(5,10,10,5),(5,10,15,15),(5,5,10,5),(5,10,15,15),(5,15,20,20),(5,10,15,10)), # subarctic
		((10,5,5,10),(30,50,50,50),(25,50,50,50),(15,30,30,30),(25,40,50,50),(20,40,50,50),(20,35,50,50)), # temperate
		((10,5,5,5),(50,50,50,50),(50,50,50,50),(35,35,35,35),(50,50,50,50),(50,50,50,50),(40,50,50,50)), # subtropical
		((5,5,5,5),(50,50,50,50),(50,50,50,50),(40,40,40,40),(50,50,50,50),(50,50,50,50),(50,50,50,50))  # tropical
	)

	climates = ('arctic', 'subarctic', 'temperate', 'subtropical', 'tropical')
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')

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
	foragemap = (
	((0,5,10,0),(5,10,10,5),(5,10,10,5),(0,0,5,0),(5,5,10,5),(10,10,15,10),(10,10,15,10)),
	((0,5,15,5),(70,85,100,75),(20,30,40,25),(10,15,20,15),(20,30,50,25),(25,35,50,35),(15,20,30,50)),
	((10,5,5,5),(80,90,100,90),(65,75,90,80),(20,30,40,30),(50,60,75,60),(50,65,80,65),(30,35,40,35)),
	((5,5,0,5),(90,100,100,100),(80,90,100,95),(40,55,75,60),(80,90,100,100),(80,90,100,95),(40,50,50,50)),
	((5,5,0,5),(100,100,100,100),(90,100,100,95),(85,90,90,90),(100,100,100,100),(90,95,100,95),(50,60,70,60))
	)
	ediblemap = (
	((0,75,75,0),(75,60,60,50),(75,60,60,50),(0,0,50,0),(50,50,50,50),(75,70,70,75),(75,70,70,75)),
	((0,50,50,75),(40,40,50,40),(50,50,40,50),(50,50,40,50),(40,4,40,50),(60,50,40,50),(60,60,60,50)),
	((70,50,70,50),(40,40,40,40),(50,40,35,50),(40,40,40,50),(40,40,30,50),(50,40,40,50),(60,50,50,60)),
	((75,80,0,75),(30,30,30,30),(30,30,25,25),(40,30,30,40),(30,30,30,35),(40,40,40,40),(60,50,50,60)),
	((75,80,0,75),(30,30,40,30),(30,40,40,35),(30,30,40,35),(30,45,50,40),(40,50,50,50),(60,60,50,60))
	)
	# the forage map is the percent chance that a normal character foraging 
	# for 2 turns will find one full day's ration of plant life (2 lbs)
	# the edible map is the percent chance that what they find is 
	# actually not edible
	# with proficiency in foraging, they find 4 lbs of food
	# and the chance of inedible is 20% less
	
	climates = ('arctic', 'subarctic', 'temperate', 'subtropical', 'tropical')
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')
	
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
		foodproblem = random.choice(('poisonous','poisonous','spoiled','tainted','spoiled','not nutritious','not nutritious','not nutritious','not nutritious'))

	return([foundfood, ediblefood, profediblefood, foodproblem])

# finding water chance
def water(climate, terrain, season):
	watermap = (
	((5,5,5,5),(10,10,10,10),(10,10,10,10),(5,5,5,5),(10,10,10,10),(10,10,10,10),(10,10,10,10)),
	((5,10,10,5),(10,20,20,10),(5,10,15,10),(5,20,15,10),(10,20,20,15),(40,60,50,50),(40,60,50,50)),
	((5,5,5,5),(30,40,30,30),(30,40,40,30),(20,20,15,20),(20,40,40,30),(60,70,80,60),(60,70,80,60)),
	((5,5,5,5),(60,70,70,60),(30,50,50,40),(40,60,50,40),(20,40,30,20),(70,80,90,70),(70,80,90,70)),
	((5,10,5,5),(80,80,80,80),(15,20,30,15),(40,70,60,70),(20,50,60,50),(70,90,90,80),(70,90,90,80))
	)
	undrinkablemap = (
	((50,50,50,50),(50,50,50,50),(50,50,50,50),(30,30,30,30),(50,50,50,50),(50,50,50,50),(50,50,50,50)),
	((60,60,60,60),(40,40,50,40),(40,40,50,40),(30,30,30,30),(50,50,50,50),(60,60,60,60),(60,60,60,60)),
	((70,70,70,80),(30,30,30,30),(40,40,50,40),(30,30,30,30),(5,50,5,50),(70,70,80,70),(70,70,80,70)),
	((70,70,80,80),(40,50,60,50),(40,40,40,40),(30,40,50,40),(50,40,40,50),(70,70,80,80),(70,70,80,80)),
	((70,70,80,80),(50,60,70,60),(40,40,50,40),(30,30,40,40),(50,50,60,50),(70,75,80,80),(70,75,80,80))
	)

	
	climates = ('arctic', 'subarctic', 'temperate', 'subtropical', 'tropical')
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')
	
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
	sheltermap = (
	(20,20,20,20),
	(90,100,100,100),
	(40,60,70,60),
	(40,40,40,40),
	(30,40,40,30),
	(40,50,50,40),
	(40,50,50,40)
	)

	
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')
	
	terrain = terrains.index(terrain)
	season = seasons.index(season)

	foundshelter = "No"

	if random.randint(0,99) < sheltermap[terrain][season]:
		foundshelter = "Yes"

	return(foundshelter)

# chance of finding medicinal plants
def medicinalplant(climate, terrain, season):
	medicinalmap = (
	((0,5,10,0),(5,10,10,5),(5,10,10,5),(0,0,5,0),(5,5,10,5),(10,10,15,10),(10,10,15,10)),
	((0,5,15,5),(70,85,100,75),(20,30,40,25),(10,15,20,15),(20,30,50,30),(25,35,50,35),(15,20,30,20)),
	((10,5,5,5),(80,90,100,90),(65,75,90,80),(20,30,40,30),(50,60,75,60),(50,65,80,65),(30,35,40,35)),
	((5,5,0,5),(90,100,100,100),(80,90,100,95),(40,55,75,60),(80,90,100,100),(80,90,100,95),(40,50,50,50)),
	((5,5,0,5),(100,100,100,100),(90,100,100,95),(85,90,90,90),(100,100,100,100),(90,95,100,95),(50,60,70,60))
	)
	usablemap = (
	((0,10,10,0),(10,10,10,10),(10,10,10,10),(0,0,20,0),(20,20,20,20),(10,20,20,10),(10,20,20,10)),
	((0,10,10,10),(30,30,20,30),(20,20,30,20),(20,20,30,20),(20,30,30,20),(10,20,30,20),(10,10,10,20)),
	((10,10,10,20),(30,30,30,30),(20,30,40,20),(20,30,30,20),(20,30,40,20),(20,30,30,20),(10,20,20,10)),
	((10,10,0,10),(40,40,40,40),(40,40,50,50),(30,40,40,30),(40,40,40,40),(30,30,30,30),(10,20,20,10)),
	((10,10,0,10),(40,40,30,40),(30,30,30,30),(40,40,30,40),(40,40,40,30),(30,40,40,30),(10,10,20,10))
	)

	# medicinal map is the chance of there being vegetation to search in
	# usable map is the chance of finding the plant

	
	climates = ('arctic', 'subarctic', 'temperate', 'subtropical', 'tropical')
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')
	
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
	fuelmap = (
	(20,20,20,20),
	(70,100,100,100),
	(40,70,70,60),
	(20,30,40,40),
	(50,70,80,70),
	(40,30,30,40),
	(40,30,30,40)
	)
	climatemodmap = (
	(-20,-10,0,-10,-20),
	(-100,-30,0,30,30),
	(-30,-20,0,10,20),
	(-40,-30,0,20,30),
	(-60,-40,0,20,20),
	(-40,-20,0,10,20),
	(-40,-20,0,10,20)
	)

	
	climates = ('arctic', 'subarctic', 'temperate', 'subtropical', 'tropical')
	terrains = ('desert', 'forest', 'hills', 'mountains', 'plains', 'coast', 'swamp')
	seasons = ('winter', 'spring', 'summer', 'fall')
	
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
		system('cls')
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
			system('cls')
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

# movement modifiers
def movement():
	system('cls')
	print("")
	print("                    Modified Movement Rate               	|	Terrain                                Movement")
	print("     Base |  12  11  10   9   8   7   6   5   4   3   2   1	|	-----------------------------------------------")
	print(" Strength |   6   5   5   4   4   3   3   2   2   1   1   1	|	0 Normal                                      1")
	print("----------+------------------------------------------------	|	1 Heavy brush or thicket                    1/3")
	print("       2  |   1   -   2   -   -   3   -   -   4   -   -   5	|	2 Light brush or forest                     2/3")
	print("       3  |   5   -   6   -   7   -   -   8   -   9   -   -	|	3 Ice or slippery footing                   2/3")
	print("                                                         	|	4 Steep slope or rough ground               1/2")
	print("     4–5  |  10  11  12  13  14  15  16  17  18  19  20  21	|	5 knee-deep snow, water, soft sand          2/3")
	print("     6–7  |  20  23  26  29  32  35  38  41  44  47  50  53	|	6 Waist-deep snow or water                  1/2")
	print("     8–9  |  35  40  45  50  55  60  65  70  75  80  85  89	|	7 Shoulder-deep snow or water               1/3")
	print("")
	print("   10–11  |  40  46  52  58  64  70  76  82  88  94 100 106")
	print("   12–13  |  45  53  61  69  77  85  93 101 109 117 125 133")
	print("   14–15  |  55  65  75  85  95 105 115 125 135 145 155 165")
	print("")
	print("      16  |  70  80  90 100 110 120 130 140 150 160 170 180")
	print("      17  |  85  97 109 121 133 145 157 169 181 193 205 217")
	print("      18  | 110 123 136 149 162 175 188 201 214 227 240 253")
	print("")
	print("18/01–50  | 135 148 161 174 187 200 213 226 239 252 265 278")
	print("18/51–75  | 160 173 186 199 212 225 238 251 264 277 290 303")
	print("18/76–90  | 185 198 211 224 237 250 263 276 289 302 315 328")
	print("18/91–99  | 235 248 261 274 287 300 313 326 339 352 365 378")
	print("18/00     | 335 348 361 374 387 400 413 426 439 452 465 478")
	print("")
	strength = input("enter a strength score or press Enter to return ")
	if strength != "":
		if strength == 18:
			exceptional = input("please enter your exceptional strength ")
			exceptional = int(exceptional)
			if exceptional in range(0,51):
				strength += 1
			elif exceptional in range(51,76):
				strength += 2
			elif exceptional in range(76,92):
				strength += 3
			elif exceptional in range(91,100):
				strength += 4
			elif exceptional == 100:
				strength += 5
		weight = input("enter a weight (whole pounds) or press Enter to return ")
		if weight != "":
			terrain = input("enter the number associated with the terrain or press Enter to return ")
			if terrain != "":
				strength = int(strength)
				weight = int(weight)
				terrain = int(terrain)
				encum_list = ((1,1,2,2,2,3,3,3,4,4,4,5),
                                (5,5,6,6,7,7,7,8,8,9,9,9),
                                (10,11,12,13,14,15,16,17,18,19,20,21),
                                (10,11,12,13,14,15,16,17,18,19,20,21),
                                (20,23,26,29,32,35,38,41,44,47,50,53),
                                (20,23,26,29,32,35,38,41,44,47,50,53),
                                (35,40,45,50,55,60,65,70,75,80,85,89),
                                (35,40,45,50,55,60,65,70,75,80,85,89),
                                (40,46,52,58,64,70,76,82,88,94,100,106),
                                (40,46,52,58,64,70,76,82,88,94,100,106),
                                (45,53,61,69,77,85,93,101,109,117,125,133),
                                (45,53,61,69,77,85,93,101,109,117,125,133),
                                (55,65,75,85,95,105,115,125,135,145,155,165),
                                (55,65,75,85,95,105,115,125,135,145,155,165),
                                (70,80,90,100,110,120,130,140,150,160,170,180),
                                (85,97,109,121,133,145,157,169,181,193,205,217),
                                (110,123,136,149,162,175,188,201,214,227,240,253),
                                (135,148,161,174,187,200,213,226,239,252,265,278),
                                (160,173,186,199,212,225,238,251,264,277,290,303),
                                (185,198,211,224,237,250,263,276,289,302,315,328),
                                (235,248,261,274,287,300,313,326,339,352,365,378),
                                (335,348,361,374,387,400,413,426,439,452,465,478))
				movement_index = 0
				for i in range(0,len(encum_list[strength-2])):
					if weight < encum_list[strength-2][i]:
						movement_index = i-1
						break
				med_movements = (12,11,10,9,8,7,6,5,4,3,2,1)
				sml_movements =  (6, 5, 5,4,4,3,3,2,2,1,1,1)

				terrain_mods = [1,0.34,0.67,0.667,0.5,0.67,0.5,0.34]

				print("\n [ {} ] / [ {} ] base move mansized/small".format(med_movements[movement_index],sml_movements[movement_index]))
				print(" [ {} ] / [ {} ] ACTUAL MOVEMENT (accounting for terrain)".format(int(med_movements[movement_index] * terrain_mods[terrain]),int(sml_movements[movement_index] * terrain_mods[terrain])))
				input("press Enter to return")



# display the rules for special combat options
def attack_options():
	system('cls')
	print('')
	print('┌─────────────┬────────────────┐  ┌──────────┐')
	print('│ Block       │ Sap            │  │ Charge   │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Called Shot │ Shield-punch   │  │ Cover    │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Disarm      │ Shield-rush    │  │ Guard    │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Grab        │ Trap           │  │ Parry    │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Overbear    │ Trap and Break │  │ Run      │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Pin         │ Unarmed Attack │  │ Sprint   │')
	print('├─────────────┼────────────────┤  ├──────────┤')
	print('│ Pull/Trip   │ Unhorse        │  │ Withdraw │')
	print('└─────────────┴────────────────┘  └──────────┘')
	print('')
	x = input('what special attack: ')
	print('')
	if x == "charge" or x == "Charge" or x == "ch":
		print("Characters and monsters can charge to rapidly close for\ncombat and make an attack. Charging is a full-move\naction, but a charging character may move 114 times his\nbase movement when he charges. A knight with a\nmovement of 6 can charge an enemy up to 9 spaces\naway.\nCharacters begin their charge on their base initiative,\nmoving up to one-half the distance of the charge. In the\nfollowing phase, they move the remainder of the dis-\ntance. Unlike most attack forms, the charge attack is\nresolved the moment the attacker arrives. If the knight\nabove has a base initiative of fast and an opponent is\nstanding 7 squares away, the knight moves 5 spaces in\nthe fast phase and 2 more in the average phase, at\nwhich point he attacks immediately.\nCharging (which might more accurately be called the\nreckless attack) gives characters several advantages but\nalso imposes some penalties. The charging character\ngains a +2 bonus on his attack roll. Some weapons,\nsuch as lances, are suited for charging and inflict\ndouble damage when used in a charge.\nBecause they are so intent on the attack, however,\ncharging characters are at a disadvantage defensively.\nThey lose all Dexterity bonuses to Armor Class and suffer\na +1 penalty to AC in addition to that. Guarding\ncharacters with weapons longer than the charger's\nautomatically strike first. In addition, characters can set\nspears (see Guard) against charges.")
	elif x == "cover" or x == "Cover" or x =="co":
		print("A character with a cocked and loaded crossbow, or an\narrow nocked and drawn in a bow, can announce that\nhe is covering an opponent within his weapon's short\nrange. The covering character can only choose to cover\na single square on the board, as long as that square is\nwithin the weapon's short range and in sight. Only characters\nwith a weapon proficiency slot in bow or crossbow\ncan cover someone in this manner. Covering\nsituations usually are created by the circumstances of\nthe initial encounter; for example, an archer may surprise\nhis enemy, cover him, and order him to drop his\nweapon. Characters can also declare a combat action\nto cover someone.\nSince the arrow or bolt is ready to be fired, the covering\ncharacter's first shot is fast (or very fast if the character\nis a specialist.) See Bows and Crossbows in\nChapter Seven. The covering character automatically\nwins initiative against the covered target. It is possible\nfor a very fast creature to beat out the shot of a proficient\narcher, but even very fast creatures can be covered\nby a specialist.\nThe character can hold his cover until later in the\nround, if he wants to see what his target is going to do.\nHe can fire first in any later phase. After the first shot\nhas been loosed, the covering character can perform\nthe rest of his missile fire at the regular action phase\nand rate of fire.\nThe covering shot itself is made with a +2 bonus to\nthe attack roll. Covering is handy for freezing opponents\nin their tracks, since everybody knows how quickly an\narrow or bolt can be released once it is drawn.\nCovering can also be used with any hand-held\nbladed weapon—basically, the character puts her\nsword to an opponent's throat in a single adjacent\nsquare and menaces him. The victim must be stunned,\ndazed, pinned, unconscious, or surprised for a character\nto cover him with a melee weapon. As with bows\nand crossbows, the covering character automatically\nwins initiative against her target and can attack in the\nfast phase, or in the very fast phase if she is a specialist.\nThe attack is made with a +2 bonus to hit, and the\ncritical number (see Critical Hits in Chapter Six) drops\nto a 16.")
	elif x == "guard" or x == "Guard" or x == "gu":
		print("When a character guards, she waits for her opponents\nto come to her. Guarding is a half-move action, or a nomove\naction if the character stands her ground. A\nguarding character strikes the moment an attacker\nmoves into the guarding character's threatening\nsquares, regardless of her actual initiative and action\nphase. The only way an enemy can attack a guarding\ncharacter first is with a longer-ranged weapon.\nIf a guarding character is attacked by a charging character,\nthe character that won initiative attacks first\n(unless one of the characters has a longer-ranged\nweapon than the other, of course). Guarding characters\nare considered to be set for charge, and spears and\nspear-like polearms inflict double damage against\ncharging creatures (see Chapter Seven).")
	elif x == "parry" or x == "Parry" or x == "pa":
		print("Sometimes the best thing to do is take cover and try\nnot to get clobbered. Any character can choose to parry\nas a combat action. Parrying is a no-move action that is\nin effect for the entire combat round. If a character parries,\nhe cannot move, attack, or cast spells.\n\nParrying reduces a nonwarrior character's Armor\nClass by one-half his level. A 6th-level wizard with an\nAC of 5 who parries reduces his AC to 2. Warriors who\nchoose to parry reduce their AC by one-half their level,\nplus one. A 6th-level fighter gets an AC bonus of 4 by\nparrying.")
	elif x == "run" or x == "Run" or x == "r":
		print("A character can double his base movement by running.\nRunning is considered a full-move action; the character\ncan't do anything else in the same combat round that\nhe runs. Running on a battlefield is dangerous; the\ncharacter loses all Dexterity bonuses to his Armor Class\nand suffers a +1 AC penalty on top of that. In addition,\nhe is considered to be charging if he runs into a square\nthreatened by an opponent with a set spear.\n\nCharacters can maintain a run as long as they have\nthe necessary fatigue points (see Fatigue, below). Outside\nof combat, they can run for a number of rounds\nequal to their Constitution score. After that, they must\nstop and rest. See Jogging and Running in the Player's\nHandbook under Chapter 14: Time and Movement for\nmore information.")
	elif x == "sprint" or x == "Spring" or x == "sp":
		print("A character can triple his base movement by sprinting.\nLike running, sprinting is a full-move action that drops\nthe character's defenses for the round.")
	elif x == "withdraw" or x == "Withdraw" or x == "with" or x == "w" or x == "wd":
		print("Withdrawing is the only safe way to leave a square that\nis threatened by an opponent. When a character withdraws,\nhe backs carefully away from his opponent without\nturning his back or creating an attack of opportunity\nfor his opponent.\n\nWithdrawing is a half-move that takes place on the\ncharacter's base initiative. A withdrawing character cannot\nattack or cast spells, although he can still get attacks\nof opportunity.")
	elif x == "block" or x == "Block" or x =="b":
		print("A character can declare that she is using one of her attacks to block an opponent's strike. Blocking is a hard parry with a weapon that deflects an opponent's attack. Any weapon except rope-like things such as nets, lassoes, or slings can be used to block.\n\nWhen a character tries to block an attack, she makes a normal attack roll against AC 4. Her opponent makes a normal attack roll against her Armor Class. The strike is blocked if the character succeeds with a lower roll than her enemy succeeded with. If the attacker failed anyway, it's a miss no matter what the blocking character rolled. If the blocking character failed but her attacker succeeded, it's a hit despite the block attempt. If the character announces her block before initiative is rolled, she can block an attack even if it beats her action phase. If she decides to wait, she can only block attacks in her action phase or later.\n\nBlocking is an excellent tactic for characters with multiple attacks to use against characters or monsters with only one attack. A rapier specialist with a main-gauche in her off hand can use her off-hand weapon or one of the rapier attacks to block while using the rest of her attacks offensively.")
	elif x == "called shot" or x == "called" or x == "cs" or x == "c s" or x == "Called Shot" or x == "Called":
		print("A called shot is an attack at a specific location on the target. For example, a called shot can be used to attack the head of an enemy who isn't wearing a helm, the unarmored legs of a character wearing only a breastplate, or the special weakness of a monster with an Achilles' heel.\n\nCalled shots have to be announced before the attack roll is made. When the called shot is announced, the character's action phase is delayed by one category; a bowshot that would normally be in the average phase becomes a slow action if the archer decides to make a called shot. If you're not playing with the initiative system described in Chapter One, assume called shots receive a +1 initiative penalty.\n\nCalled shots normally present the attacker with a\n - 4 penalty on his attack roll, but the DM can modify this for the circumstances. If the target is surprised or not expecting the attack, the called shot modifier may not apply at all. On the other hand, a particularly difficult called shot (stabbing an enemy through the eyeslit of his visor, for example) may inflict a\n - 6 or even a\n - 8 penalty to the attack roll. Called shots are disrupted if the character attempting it suffers a knockdown.\n\nAlthough called shots are normally most useful for special combat effects, like breaking a beaker of acid in an evil wizard's hand, they can also be useful against partially unarmored opponents. An enemy in full plate mail with no helmet has an AC 10 head; it's easier to make the called shot with a\n - 4 penalty against that AC 10 than to swing at the enemy's normal AC of 1. If a called shot is used to strike a specific body area and results in a critical hit, ignore the location die of the critical hit roll and just roll the effect for the area struck. (See Chapter Six for more information on critical hits.)\n\nCalled shots can also be used to fire missile weapons into a melee without the risk of hitting an ally. If the called shot misses, no one else is in danger of being hit by the missile.\n\nAs an optional rule, the DM may allow called shots to be used to force an automatic retreat or knockdown effect, rather than inflict damage.")
	elif x == "disarm" or x == "Disarm" or x == "d":
		print("There are two types of disarming maneuvers, offensive and defensive, and they both work essentially the same way. A character who wishes to use either type of disarm must allocate one of his attacks for the round to the feat. If the disarm is a defensive one, it is resolved before the attacker rolls to hit. A disarm works very much like a block, but the character attempting the disarm must roll against AC 0, while the intended victim of the disarm still rolls against an AC 4.\n\nAnyone involved in a disarm that is using a two-handed weapon receives a 4-point bonus to the target Armor Class for the purposes of the opposed roll. It's impossible to disarm a weapon two sizes larger than your own, so a fighter with a dagger can't try to disarm a mage with a quarterstaff. Disarming can occur using a missile weapon, but the missile's size is the factor used to determine whether or not the attempt can succeed, not the weapon firing the missile.\n\nDefensive disarms work just like blocks for initiative; if announced before the roll, they can be attempted against attacks that beat the character's action phase. Otherwise, they can only be used on the character's action phase or later in the round. Offensive disarms work like called shots; when announced, they delay the character's action phase by one step. The intent to disarm has to be announced before any rolls are made.\n\nWhen a weapon is disarmed, it falls 1-10 feet away ( I d 3\n - 1 squares) in a random direction. Recovering a disarmed weapon requires a half-move. A disarmed character can be immediately covered if the attacker has an attack remaining in the round. Disarms work best against low-level opponents who don't have good THACOs, since it's difficult for them to make their opposed rolls.")
	elif x == "grab" or x == "Grab" or x == "g":
		print("Characters can grab weapons or important items away from their opponents. If the character wants to grab his opponent directly, he should consider it a wrestling attack and resolve it as unarmed combat; see Chapter Five. A character has to have a hand free to grab; if both hands are full, he's got to drop something in order to attempt the grab. (Two-handed weapons can be held in just one hand, but the character can't attack this way.) The attacker must announce the grab attempt before he makes his attack roll.\n\nTrying to grab an enemy's possessions while he threatens you is a bad idea; the defender receives an immediate attack of opportunity against the grabber.\n\nGenerally, the grab attempt works the same way a disarm attempt does. The character attempting to grab an item must make an opposed roll against AC 0 while the intended victim rolls against AC 4. The DM may assign certain penalties to the character attempting the grab, depending on circumstances; grabbing a tiny ring on someone's finger might incur a\n - 8 penalty to the target Armor Class for the grabbing character. If the opposed roll results in a tie, the item may be dropped or broken at the DM's discretion.\n\nOnce the grabbing character succeeds in grasping the item, the opponents must wrestle for control of it using opposed Strength checks. If a character only grabs (or was originally holding) the item with one hand, then his Strength is reduced by 3 points")
	elif x == "overbear" or x == "over" or x == "Over" or x == "Overbear" or x == "o" or x == "ob":
		print("Overbearing includes most attacks aimed at simply overpowering the target. If the attackers are seeking to overwhelm the defender through brute strength or sheer weight of numbers, it's an overbearing attack.\n\nOverbearing includes most attacks aimed at simply overpowering the target. If the attackers are seeking to overwhelm the defender through brute strength or sheer weight of numbers, it's an overbearing attack.\n\nOverbearing is a tactic available to any creature and can be used against almost any other creature. Creatures with multiple legs are difficult to overbear. Creatures with no legs at all are nearly impossible to overbear (because they can't be knocked down) but attackers with sufficient strength sometimes can pin them in place. Creatures with no solid form (immaterial, gaseous, or liquid) cannot be overborne. Characters need not have their hands free to make overbearing attacks, but they might not be able to take full advantage of pins if they do not (see below). \n - 4-point bonus or penalty per size difference of the attacker and defender \n - +1 bonus per additional attacker \n - -4 penalty if defender has more than two legs \n - -4 penalty if the defender is legless \n - -8 penalty if the defender is amorphous and legless\n\nIf the defender wins the opposed Strength roll, she stays on her feet and the attackers remain in their squares. The defender remains clear and can finish the round normally. If the attackers win, they (or as many as will fit) enter the defender's square and everyone falls in a heap with the attackers on top. The overborne character takes no damage. Note that attackers in squares adjacent to the defender can contribute to overbearing attacks even if they can't enter the defender's square.\n\nIf defender is overborne, she loses all actions for the remainder of the round and her actions are severely limited the next round; the character is grappled and cannot move or make any attacks (including attacks of opportunity) until she gets free.\n\nA defender who has been knocked down by an overbearing attack can be pinned if she is successfully overborne again in the following round. Overborne defenders can do nothing until the pin is resolved.")
	elif x == 'p' or x == 'pin' or x == "Pin":
		print("Attackers who have made successful overbearing attacks have an advantage over the defender in the following round. The attackers can release the opponent or try for a pin. If the attackers release the opponent, they can immediately attempt another unarmed attack, draw a weapon and attack (this counts as a half-move action), or attempt some other action normally available to characters, such as movement. If the attackers try for a pin, conduct another opposed Strength roll. If the attackers win, the opponent is pinned (see below). If the defender wins, the attackers must leave the defender's square and the defender can spend a half move or an attack to stand up, just as if she had suffered a knockdown.\n\nAttackers who have made successful overbearing attacks have an advantage over the defender in the following round. The attackers can release the opponent or try for a pin. If the attackers release the opponent, they can immediately attempt another unarmed attack, draw a weapon and attack (this counts as a half-move action), or attempt some other action normally available to characters, such as movement. If the attackers try for a pin, conduct another opposed Strength roll. If the attackers win, the opponent is pinned (see below). If the defender wins, the attackers must leave the defender's square and the defender can spend a half move or an attack to stand up, just as if she had suffered a knockdown.\n\nEffects of Pins A pin lasts for an entire combat round. A pinned character is considered prone and grappled. The attackers can immobilize a pinned character's limbs if their hands are free. If the attackers are the same size or larger than the defender, one of the defender's limbs is immobilized and useless for every attacker with free hands in the pile. If the attackers are smaller, it takes one extra creature per size class difference to immobilize a limb. For example, it takes one human to hold down an ore's arm, two humans to hold down an ogre's arm, and three humans to hold down a hill giant's arm. If the attackers are larger, they can pin two limbs for every two size classes difference. For example, a single ogre can pin one limb of a dwarf or two of a halfling's limbs. If all the defender's limbs are immobilized for two consecutive rounds, the attackers have the upper hand and can choose any wrestling lock effect. (Damage from locks achieved through an overbearing pin is mostly temporary, as in all other forms of brawling combat.) A group that achieves a lock inflicts damage only once per round, but uses its effective group Strength score when determining damage.\n\nMaintaining and Breaking Pins A pinned creature can make unarmed or natural attacks with its free limbs or can attack with a size S weapon. The pinned character's original facing does not affect these attacks; all the characters involved are entangled in a random dogpile and the defender is assumed to be facing all the attackers simultaneously—this is one disadvantage to overbearing attacks. If the defender inflicts a critical hit with a weapon or natural attack, he can opt to inflict double damage (or roll for a special effect according to the rules presented in Chapter Six) or force the attacker who is struck to release her. If the defender scores a knockdown with a pummeling or weapon attack, the attacker who is struck must release the defender. The attacker cannot directly counter the pin, she must wait until the attackers try to maintain the pin. Attackers who have pinned a defender must make an opposed Strength roll each round to maintain the pin. If a pinned defender wins the opposed Strength roll, she breaks the pin and can spend a half move or an attack to stand up. She is still grappled, however. If the defender wins the next opposed Strength roll, she breaks free. If the defender wins initiative, she can force the roll herself on her attack phase; this is the only time a defender can initiate the opposed roll, which can be either an attack or a Strength roll, at the defender's option. If the defender loses or there is a tie, the defender remains grappled and the attackers can skip the attack roll and go directly to the opposed Strength roll on their next action phase. If the defender wins, she breaks free and can finish the round normally.\n\nAssistance Overbearing involves brute force and is the natural attack form for groups of creatures confronting a lone target. In the case of multiple defenders, the attackers can divide themselves among their opponents or concentrate on a single defender, provided that the attackers occupy squares adjacent to the defender. The defender's allies, if clear, can remove attackers from the pile by making overbearing or wrestling attacks against them. An ally who threatens the attackers can make attacks of opportunity each time the attackers initiate an opposed roll—the arrival of an armed ally usually breaks up a massed overbearing attack. A critical hit or knockdown can force an attacker to release a defender, as described above. Missile attacks directed at a pile have a chance to hit any character in the pile as described in Chapter One.")
	elif x == "pull" or x == "Pull" or x == "t" or x == "trip" or x =="Trip" or x == "pull/trip" or x == "pt" or x == "p/t" or x == "p t":
		print("A good tactic against moving enemies or characters who aren't paying attention is a trip or tangling maneuver. To pull or trip an opponent, the character must be armed with a weapon that has the ability to snare someone's legs. The following weapons all qualify: bill, bola, bow, light or heavy crossbow, horseman's flail, harpoon, javelin, khopesh, lasso, mancatcher, net, footman's or horseman's pick, any polearm, quarterstaff, scourge, spear, staff sling, and whip. These weapons feature long, staff-like pieces, chains or ropes, or heads that can catch and pull an enemy's legs out from under him.\n\nTo pull or trip an enemy, the character makes a normal attack roll. If he hits, he makes an opposed roll of his Strength against the defender's Dexterity or Strength, whichever is better. If the attacker wins, the defender is knocked down. If the defender wins or if both fail, the attack fails. If the roll is a tie, they both fall down.\n\nFor purposes of this maneuver, a monster's normal movement rate can be considered its Dexterity score. Its Strength is equal to 314 points per size plus its Hit Dice. There are several modifiers that apply to the attacker's Strength, however: \n - 4-point bonus or penalty per size difference \n - -2 to attacker's strength if the target has four legs or more \n - +3 if the defender was unaware of the pull or trip attack \n - -6 if the defender was stationary\n\nOptionally, the opposed roll can be replaced by a simple saving throw vs. paralyzation. It's not as accurate, but it may be more convenient for the DM and players to remember.")
	elif x == "sap" or x == "Sap" or x == "s":
		print("Sapping is an attempt to knock out an opponent by striking with the flat of the blade or slugging him from behind with a sturdy sword-hilt. It doesn't work very well against characters or monsters that are expecting it; any character attempting to sap a creature that threatens her provokes an attack of opportunity for the defender. Hand-held weapons and thrown weapons may be used in sap attempts.\n\nA sap is a type of called shot; it has a one-phase initiative penalty, and the attacker has a\n - 4 penalty to hit The penalty increases to\n - 8 if the defender is wearing some kind of helmet. Only Small or Medium creatures can be sapped; Large monsters can't be knocked out like this.\n\nIf the attacker scores a hit, she may knock out her opponent. There is a 5% chance per point of damage of knocking out the victim, up to a maximum of 40%. Thus, if the sapper inflicts 5 points of damage, she has a 25% chance of knocking out her opponent. Sapping damage is like unarmed combat damage; 25% is real and the rest is temporary. Naturally, if her damage roll exceeds the victim's hit points, he's knocked out anyway.\n\nThe knockout chance increases to 10% per point of damage (max 80%) if the victim is surprised, asleep, restrained, or magically held in some way. Sapped characters remain unconcious for 3d 10 full rounds.")
	elif x == "shield-punch" or x == "shield punch" or x == "sp" or x == "s p":
		print("Any character equipped with a shield can choose to forego its protection and gain an extra attack known as a shield-punch. The shield-punch is treated as a normal, secondary weapon attack; the primary weapon suffers a\n - 2 penalty to attack rolls that round and the shield-punch attack is rolled with a\n - 4 penalty. A character may use his reaction adjustment due to a high Dexterity score to offset these penalties. Alternatively, the character can substitute his normal attack for a shield punch, with no penalties.\n\nThe exact characteristics (i.e., damage and speed) of each type of shield are noted in Chapter Seven. If the character is trying a shield-punch, he must announce his intention while declaring his combat action and forfeits the defensive benefit of the shield for the round. The character moves into the square of his opponent on his base initiative, then executes the shield punch and backs out into his own square again on the following initiative phase.")
	elif x == "shield-rush" or  x == "shield rush" or x == "sr" or x == "s r":
		print("The shield-rush is an attempt to knock someone down by running into them with your shield. The character must have 10 feet (2 spaces) of running room to make an effective shield-rush. Making a shield-rush is treated as a charge attack for purposes of guarding characters with set spears.\n\nWhen the character makes a shield-rush, he makes a normal attack against his enemy's AC. Some shields may provide modifiers or bonuses to the rush; refer to Chapter Seven. After a shield has been used for a rush, it provides no AC bonus for the rest of the round for its bearer. Making a shield-rush also costs the character a normal attack, but it isn't considered an off-hand weapon like a shield-punch.\n\nIf the shield-bearer hits with his attack, he makes an opposed Strength roll against his opponent to see if he knocks him down. The loser of the opposed roll falls down; if both characters fail their Strength rolls, they both fall down. The following modifiers apply to the attacker's Strength score: \n - 4-point bonus or penalty for each size difference \n - +3 if defender is unaware of shield-rush \n - -2 if the dfender has four legs or more\n\nAs noted before, monsters can be assumed to have a Strength of Vk per size category plus their Hit Dice. Instead of an opposed roll, the DM can substitute a saving throw vs. paralyzation for the defender to save time.\n\nIf the shield-rusher misses with his attack roll, he must roll a successful Dexterity check to stay on his feet as he rushes past his target. If he fails, he falls down.")
	elif x == "trap" or x == "t":
		print("It's possible to use your weapon or shield to pin your enemy's weapon against his body or to trap the weapon on your own sword-hilt or weapon haft. This maneuver is known as a trap. Traps are much like blocks; the character can get a chance to trap an attack that comes before his action phase by declaring the trap before initiative is rolled, or he can trap any attack that comes in his action phase or later without declaring his action beforehand.\n\nLike with a disarm, the trap is resolved before the normal attack roll is made. A character attempts to trap an enemy's attack by rolling an opposed attack roll versus AC 0 while his opponent rolls against AC 4. If the trapping character wins the opposed roll, the weapon is successfully pinned. Otherwise, the pin fails and the normal attack roll is made.\n\nOnce an enemy's weapon is trapped, he loses any additional attacks he could have made with that weapon in the current round. At the end of the round, the trapping character and his victim make opposed Strength rolls to see if the victim can free his weapon. In each subsequent round, one Strength check is made on the fastest character's base initiative, and a second one at the end of the round.\n\nA character with a trapped weapon can always attack with a secondary weapon or simply abandon the weapon that's been caught. The character who performs the trap cannot use the weapon or shield he's pinning the opponent's weapon with.\n\nTrapping is an excellent tactic to use against an opponent with fewer attacks. It is also a good tactic for a two-weapon fighter to use against a single-weapon fighter; by sacrificing one weapon's attacks, he completely stops his opponent's offense. Another sneaky trick is to have an ally trap a tough opponent's weapon to free up unanswered flank or rear attacks for a second character. Trapping is tougher than a simple block, but worth the effort.")
	elif x == "trap and break" or x == "Trap and Break" or x == "tb" or x == "t and b" or x == "t b":
		print("Some weapons, such as the sai or the swordbreaker, are suited for breaking a trapped enemy weapon. When a weapon of this type is used to trap an enemy weapon, the trapping character can declare an attempt to break the weapon. The trapped character must roll a successful item saving throw vs. crushing blow for his weapon or it breaks; for metal weapons, this is a 7 or better on 1 d20. The weapon's magical bonus applies.\n\nIf the break attempt fails, the trapped blade is automatically freed. Otherwise, the weapon is broken. Only swords, knives, or weapons with sword-like components (such as a halberd's spike or a glaive) can be broken.")
	elif x == "unarmed" or x =="Unarmed Attack" or x == "ua" or x == "unarmed attack" or x == "u a":
		print("Throwing a punch or trying to get a wrestling hold on the enemy is always a legitimate attack. As noted in Chapter One, trying to engage an armed opponent in unarmed combat is risky; if the armed character threatens the attacker, he gets an immediate attack of opportunity. There are several types of unarmed attacks that can be employed by a character, including punching, wrestling, martial arts, and overbearing. The various types of unarmed combat are described in great detail in Chapter Five. Note that a character has to have a hand free to punch or wrestle someone.")
	elif x == "unhorse" or x == "Unhorse" or x == "un" or x == "uh":
		print("A mounted enemy can be knocked off his steed by a number of methods. Whenever a character is in danger of falling off his horse, he must roll a successful riding proficiency check (or a saving throw vs. paralyzation if he doesn't have the riding proficiency) to remain in the saddle. If he fails, he's considered to be knocked down and is lying prone on the ground. \nSome ways to unhorse a mounted character include:\n - Knockdown: Striking a mounted character or the mount hard enough to create a knockdown chance;\n - Damage: Striking a mounted character for 10 or more hit points of damage; \n - Pull/Trip: Hitting a mounted character or the mount itself with a pull/trip attack; \n - Overbearing: Successfully grappling a mounted character with an overbearing attack (he may also be pulled down by losing the opposed Strength check to fight off the overbearing attempt); \n - Damage to the Mount: Wounding a mount during the battle (killing the steed always unhorses a character, no questions asked).")
	input('press Enter to return')

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

	daylightmap = (
	(7.5, 21.5, 23.5, 24, 24, 22, 17.5, 4.5, 1, 0, 0, 2.5), # arctic
	(11.5, 14.5, 17.5, 19.5, 18, 16, 13, 10, 7, 5.5, 5.5, 9), # subarctic
	(12, 13, 14.5, 15.5, 14.5, 14, 12.5, 11, 9.5, 9, 9.5, 10.5), # temperate
	(12, 12.5, 13, 13.5, 13.5, 13, 12, 11.5, 11, 10.5, 11, 11.5), # subtropical
	(12, 12.5, 12.5, 12.5, 12.5, 12.5, 12, 12, 11.5, 11.5, 11.5, 12) # tropical
	)

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

	system('cls')
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

	system('cls')
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
	system('cls')
	print('                                           Proficiencies')
	print('===========================================================================================================================================')
	print(' 1  Agriculture          20  Endurance             37  Mining                55  Survival                  84  Acting')
	print(' 2  Ancient History      21  Engineering           38  Mountaineering        56  Swimming                  85  Chanting')
	print(' 3  Animal Handling      22  Etiquette             39  Musical Instrument                                  86  Craft Instrument')
	print(' 4  Animal Lore                                                              57  Tightrope Walking         87  Crowd Working')
	print(' 5  Animal Training      23  Fire-building         40  Navigation            58  Tracking                  88  Poetry')
	print(' 6  Appraising           24  Fishing                                         59  Tumbling                  89  Whistling/Humming')
	print(' 7  Armorer              25  Forgery               41  Pottery                                                 ')
	print(' 8  Artistic Ability                                                         60  Ventriloquism             90  ')
	print(' 9  Astrology            26  Gaming                42  Reading Lips                                        91  ')
	print('                         27  Gem Cutting           43  Reading/Writing       61  Weaponsmithing            92  ')
	print('10  Blacksmithing                                  44  Religion              62  Weather Sense             93  ')
	print('11  Blind-fighting       28  Healing               45  Riding, Airborne      63  Weaving                   94  ')
	print('12  Bowyer/Fletcher      29  Heraldry              46  Riding, Land-Based                                  95  ')
	print('13  Brewing              30  Herbalism             47  Rope Use              64  Alterness                 96  ')
	print('                         31  Hunting               48  Running               65  Animal Noise              96  ')
	print('14  Charioteering                                                            66  Begging                   97  ')
	print('15  Cobbling             32  Juggling              49  Seamanship            67  Boating                   98  ')
	print('16  Cooking              33  Jumping               50  Seamstress/Tailor     68  Fast-Talking              99  ')
	print('                                                   51  Set Snares            69  Fortune Telling          100  ')
	print('17  Dancing              34  Languages, Ancient    52  Singing               70  Information Gathering    101  ')
	print('18  Direction Sense      35  Languages, Modern     53  Spellcraft            71  Intimidation             102  ')
	print('19  Disguise             36  Local History         54  Stonemasonry          72  Locksmithing             103  ')
	print('                                                                             73  Looting                  104  ')
	print('                                                                             74  Observation              105  ')
	print('                                                                             75  Trailing                 106  ')
	print('                                                                             76  Voice Mimicry            107  ')
	print('                                                                             77                           108  ')
	print('                                                                             78                           109  ')
	print('                                                                             79                           110  ')
	print('                                                                             80                           111  ')
	print('                                                                             81                           112  ')
	print('                                                                             82                           113  ')
	print('                                                                             83                           114  ')
	p = input("what proficiency? ")
	with open('proficiencies/proficiencies.txt') as prof_file:
		prof_file = prof_file.readlines()
	p = prof_file[int(p)-1]
	p = p.split('\\n')
	step = 31
	b = int(len(p)/step) + 1
	page = 1
	for i in range(0,len(p),step):
		system('cls')
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

# Combat Modifiers
def combat():
	system('cls')
	print('')
	print('                           Cover Modifiers')
	print('                  Target is     Cover    Concealed')
	print('                        25%        -2           -1')
	print('                        50%        -4           -2')
	print('                        75%        -7           -3')
	print('                        90%       -10           -4')
	print('')
	print('                          Combat Modifiers')
	print('┌───────────────────────────────┬──────────────────────────────────┐')
	print('│ Attacker on high ground :  +1 │     Defender stunned/prone :  +4 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│      Defender invisible :  -4 │         Defender surprised :  +1 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│    Defender off-balance :  +2 │   Missile fire, long range :  -5 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│  Defender sleeping/held :   X │ Missile fire, medium range :  -2 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│    Defender kneeling :  +1/-2 │    Defender laying down :  +4/-2 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│     Defender sitting :  +2/-2 │    Attacker using off-hand :  -2 │')
	print('├───────────────────────────────┼──────────────────────────────────┤')
	print('│             Flank attack : +1 │                Rear attack :  +2 │')
	print('└───────────────────────────────┴──────────────────────────────────┘')
	print('  X - automatically hits. if')
	print('      not in combat, defender')
	print('      is slain automatically.')
	input('\npress Enter to continue to CLIMBING MODIFIERS ')

	print("")
	print("Climbing Modifiers")
	print("- Dex and Shield AC bonuses are lost")
	print("- Attacks against climbers have a +2 Rear Attack bonus")
	print("- Climbers suffer -2 to attack, damage, and saving rolls")
	print("- Attacking from above/below is a +2/-2 bonus")
	print("- Two-handed weapons are rarely usable")
	print("- Any damage triggers a climbing check. Unassisted climbers")
	print("  fall but assisted climbers can't attack, have a -2 to")
	print("  saving throws, and attacks against them are +2")
	input("\npress Enter to return")

def displayNew(rain,wind_max,day,weekday,month,monthday,\
	hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
	wind_low,wind_missile,wind_melee,wind_move,viz_day,\
	viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season,food_list):
	
	dawn, dusk, dl = daylight(day,climate)

	console = Console()
	
	def make_layout() -> Layout:
	    """Define the layout."""
	    layout = Layout(name="root")
	
	    layout.split(
	        Layout(name="header", size=3),
	        Layout(name="main", size=28),
	        Layout(name="footer", size=5),
	    )
	    layout["main"].split_row(
	        Layout(name="side"),
	        Layout(name="body", ratio=2, minimum_size=60),
	        Layout(name="three", ratio=1)
	    )
	    layout["side"].split(Layout(name="box1"), Layout(name="box2"), Layout(name="box3")),
	    layout['three'].split(Layout(name="combat"), Layout(name="morale", size=12)),
	    layout['body'].split(Layout(name="topmid", ratio=3), Layout(name="bodylow", ratio=10)),
	    layout["bodylow"].split_row(Layout(name="wilderness", ratio=3), Layout(name="foodlist", ratio=2))
	    layout['topmid'].split_row(Layout(name='weather', ratio=3), Layout(name="daylight",ratio=2))
	    return layout
	
	# resizing everything
	for i in range(0,4-len(eff_hi)):
		eff_hi = " " + eff_hi
	for i in range(0,4-len(eff_lo)):
		eff_lo = " " + eff_lo
	for i in range(0,4-len(hi)):
		hi = " " + hi
	for i in range(0,4-len(lo)):
		lo = " " + lo
	for i in range(0,4-len(day)):
		day = " " + day
	if len(monthday) < 2:
		monthday = " " + monthday
	for i in range(0,13-len(month)):
		month += " "
	for i in range(0,12-len(climate)):
		climate += " "
	for i in range(0,12-len(terrain)):
		terrain += " "
	for i in range(0,12-len(season)):
		season += " "

	food_string = ''
	for i in range(0,len(food_list)):
		if i < 9:
			food_string += " " + str(i+1) + " "
		else:
			food_string += str(i+1) + " "
		if food_list[i][3] == "":
			food_string += "    "
		else:
			food_string += food_list[i][3] + " "
		food_string += food_list[i][0] + '\n'


	layout = make_layout()
	layout["header"].update(Panel('reading from file: {}'.format(file)))
	layout["weather"].update(Panel('  hi     lo  |  {}\n{}   {}  |  {}\n{}   {}  |  humidity: {}%\n             |'.format(rain,eff_hi,eff_lo,spec,hi,lo,humiditymod), title="Weather"))
	layout["daylight"].update(Panel('{} dawn {}\n{} dusk {}\n{}    h {}'.format(climate,dawn,terrain,dusk,season,dl), title="Daylight & Setting"))
	layout["box1"].update(Panel("             {} mph\n{}\n\n     missiles  {}\n        melee  {}\n         move  {}".format(wind,winddir,wind_missile,wind_melee,wind_move), title="Wind"))
	layout["box2"].update(Panel("{} {}        (d {})\n   {}\n─────────────────────────────────\n      day {} yds\n twilight {} yds\nmoonlight {} yds\n     dark {} yds".format(monthday,month,day,weekday,viz_day,viz_twi,viz_moon,viz_dark), title="Calendar & Visibility"))
	layout["box3"].update(Panel("\n             <50  <70  <90   +\n    inactive   5    6    7   8\n       light   6    7    8  10\n    moderate   8    9   10  12\n       heavy   9   10   12  16\n\n\t\t     (in pints)", title="Water Minimums"))
	layout["combat"].update(Panel("   Attacker on high ground  1 \n    Defender stunned/prone  4\n        Defender invisible -4 \n        Defender surprised  1\n      Defender off-balance  2 \n    Defender sleeping/held  X \nMissile fire, medium range -2\nMissile fire,   long range -5\n         Defender kneeling  1 \n      Defender laying down  4\n          Defender sitting  2 \n   Attacker using off-hand -2\n               Rear attack  2\n              Flank attack  1", title="Combat"))
	layout["wilderness"].update(Panel('hunting : {}\n\nfishing : \n{}\n{}\n{}\n{}\n\nforaging :\n   regular forager : {}\nproficient forager : {}\n           problem : {}\n\nwater : {}, {}\nnatural shelter : {}\nfuel : {}\n\nmedicial plants :\n   regular forager : {}\nproficient forager : {}'.format(wilderness[0][1],wilderness[1][0],wilderness[1][1],wilderness[1][2],wilderness[1][3],wilderness[2][1],wilderness[2][2],wilderness[2][3],wilderness[3][0],wilderness[3][1],wilderness[4],wilderness[6],wilderness[5][1],wilderness[5][2]), title='Surrounding Wilderness'))
	layout["foodlist"].update(Panel(food_string, title='Food List'))
	layout["morale"].update(Panel('  surprised\n  superior force\n  ally slain by magic\n  1/4 group fallen\n  1/2 group fallen\n  " " " & ally falls\n  tempted (bribe, &c)\n  covering rear guard\n  use magic charge\n  surrounded', title="Morale Checks"))
	layout["footer"].update(Panel("  d : go to a specific day    1 : add 1 day                     f : add/remove food    m : morale check    t : gen treasure    sp : special attack\n  l : new location            s : change location parameters    p : show plants        i : initiative     po : poison info\n sd : market forces          pr : look up proficiency           c : combat mods       sa : save          mov : movement"))

	console.print(layout)


def main(f,d,wilderness,climate,terrain,season,food_list):
	x = f[d]
	#display(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],\
	#	x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],\
	#	x[17],x[18],x[19],x[20],x[21],\
	#	wilderness,climate,terrain,season,food_list)
	displayNew(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],\
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
	x = input("enter command: ")
	if x == "d":
		x = input("what day: ")
		prev_day = d
		d = int(x)
		season = update_season(d)
	elif x == "mov":
		movement()
	elif x == "sp":
		attack_options()
	elif x == "t":
		treasure_gen()
	elif x == "x":
		print(wilderness)
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
	elif x == "po":
		poison()
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