import random

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
	
	
	code = input("what treasure letter?\n")
	
	
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
		ornamental = ["Azurite: Opaque, mottled deep blue", "Banded Agate: Brown, blue, red, and white stripes", "Blue Quartz: Transparent pale blue", "Eye Agate: Gray, white, brown, blue, and green circles", "Hematite: Gray-black", "Lapis Lazuli: Light or dark blue with yellow flecks", "Malachite: Striated light and dark green", "Moss Agate: Pink, yellow-white with gray-green moss-like markings", "Obsidian: Jet black", "Rhodochrosite: Light pink", "Tiger Eye Agate: Rich golden brown with dark striping", "Turquoise: Aqua with darker mottling"]
		semiprecious = ["Bloodstone: Dark gray with red flecks","Carnelian: Orange to red-brown","Chalcedony: White","Chrysoprase: Translucent apple to emerald green","Citrine: Pale yellow brown","Jasper: Blue, black to brown","Moonstone: White with pale blue hue","Onyx: Black, white, or bands of both","Rock Crystal: Clear, transparent","Sardonyx: Bands of red and white","Smoky Quartz: light gray, yellow, brown or blue","Star Rose Quartz: Smoky rose with white star center","Zircon: Clear pale aqua"]
		fnacy = ["Amber: Transparent golden", "Alexan"]
		fancy_precious = ["Amber: Transparent golden","Alexandrite: Dark green","Amethyst: Purple crystal","Aquamarine: pale blue green","Chrysoberyl: green or yellow green","Coral: Pink to crimson","Garnet: Deep red to violet crystal","Jade: Light to dark green or white","Jet: Deep black","Pearl: Pure white, rose, to black","Peridot: Olive green","Spinel: Red, red-brown, green, or deep blue","Topaz: Golden yellow","Tourmaline: Pale green, blue, brown, or red"]
		gems_jewels = ["Black Opal: Dark green with black mottling and golden flecks","Black Sapphire: Rich black with highlights","Diamond: Clear blue-white, rich blue, yellow, or pink","Emerald: Brilliant green","Fire Opal: Fiery red","Jacinth: Fiery orange","Opal: Pale blue with green and gold mottling","Oriental Amethyst: Deep purple","Oriental Emerald: Bright green","Oriental Topaz: Fiery yellow","Ruby: Clear to deep crimson red","Sapphire: Clear to medium blue","Star Ruby: Translucent ruby with white star highlights","Star Sapphire: Translucent blue with white star highlights"]
	
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
	
		objetsdart = ["A beautiful elven vase that is slightly cracked. The painting around the outside of the vase depicts an elven god planting the world’s very first tree.", "Artwork of a battle showing the local lords fighting off an attack, painted by a long dead artist. The painting is set in a lovely gold leaf frame.", "A child’s painting framed beautifully. The art itself is fairly lacking but the frame is worth a decent amount, even more to someone who appreciates the juxtaposition of incredibly classy and messy.", "A jade tea set for two, stored on a lovely wooden tray.", "A large stone that (magically/naturally) glows. It is crafted into a statuette of a celestial being. The stone itself is worth little but the craftsmanship is very fine.", "A baby’s blanket made of the finest cloth. It is kept in a mothballed container for years. It smells faintly of mint, as if someone meant to store it for a very long time.", "A model of the solar system you reside in. It is made entirely out of brass with some of the labels faded over time. It could possibly be sold to a place of knowledge for a slightly higher price.", "A finely made flask and flask sheath. The flask is slightly dirty on the inside but with some running water and time, it will reveal a noble’s crest on the side immediately, skyrocketing the value.", "A deed to a very small portion of land that now resides in the very middle of a noble’s house. The city will buy it off of you for a good price.", "A golden likeness of the hand of a legendary female warlord, sitting atop a small pedestal bearing her name (Alanna the Fearless). The hand is able to hold a sword that is made to her specific specifications, all others simply fall out.", "A jade carving of a dog etched with its eulogy.", "Two delicate links of silver chain around a demon statuette of rare wood. Of particular interest to that demon’s cult.", "Seven beautifully etched bells in descending sizes, each made of silver and each with its own tone. Ringing one makes you slightly sleepy, others fill you with talkative urge or a powerful sense of unease.", "A handful of jasper puzzle pieces speckled with flecks of semiprecious stone (citrine, amethyst, garnet, etc.) that assemble themselves into the 2-D likeness of the last animal you pointed at.", "A painting of middling skill drawn by a local lord who has recently passed. “He was a bastard when he was alive. but an endearing one now he’s dead!”", "A painting of exquisite skill drawn by a discredited masterandom. “Hm… probably a fake. I’ll give you 100 gold, consider yourself lucky.”", "A palm-sized bronze automaton of a goose that lays a copper egg. Its eyes are rubies. Feed it copper coins and it produces more copper eggs.", "A small sapphire hairpin carved into the shape of an ocean wave.", "A volume of poetry by the late great bard _______.", "A volume of painstakingly illuminated holy scripture – bookmarked to some of the racier passages.", "A beautifully crafted but unbalanced and obviously impractical weapon. Is it a long-handled sword? A short-handled spear with a long blade? A throwing javelin with a 10-foot range?", "A silver and brass mirror with lewd designs hidden around the frame.", "The gaudy holy symbol of a cult to the defunct goddess of wealth.", "A small notebook with the random musings of ‘The Authorandom.’ Many of them pertain about the nature of the world, time, space and the future. Oddly no one has noticed that all the predictions in said notebook have come true.", "A crudely made painting of a king smiling. The painting itself is nothing special. What is however special is the painter but being one of his worse works it gets a rather low price.", "The (nonmagical) axe of Gunthar the Brave, a hero that is very well known and celebrated in his hometown, but not very well known elsewhere.", "A fancy belt buckle (broken beyond repair) from a legendary wizard hero, engraved with his initials.", "A set of candlesticks that on casual glance look extremely expensive which, upon very close examination, turn out to be made of brass instead of gold and with glass instead of gemstones.", "An exquisite scrimshaw design of dueling dragons made from a harpy claw.", "A chunk of metal that, when inspected, is just 100 gp melted and welded togetherandom.", "A clay pot full of a rare and valuable spice.", "A ridiculously unusable gold-plated fantasy sword.", "A canvas swatch full of lines and streaks of colors, all of which methods of color reproduction are lost to time.", "A round table with engraved magic circle and runes that casts a random Prestidigitation effect every day on a fixed lantern in the middle of the table.", "A blue-blade sword within a black leather sheath trimmed with silver leaves. It can be pulled out, but not drawn all the way out.", "A 2-foot golden statue of the deity Waukeen. Waukeen is seated on a chair made of coins.", "The beautifully carved silver lance tip of Sir Thais. It had tipped his ceremonial lance, which was all he had when the [insert current npc group the PCs just fought] brazenly ambushed the king’s parade a few months ago. The tip broke off after being plunged into the shoulder of [a bad guy] and was recovered by [bad guy minions]. Sadly, being ceremonial, the designs are intricate but not really effective for a lance tip, nearly blunt.", "A silver ring with a small piece of jet set in it.", "Boots that magically stay warm and dry, no matter what they’ve been through.", "A filigree gold goblet once owned by a prince.", "An amphora of ancient Fey wine (still good, and very tasty).", "A crown of wyvern fangs set in silverandom.", "A white cape with red embroidery. As you spill blood on the cape, the embroidery grows.", "A silver lined demon skull drinking cup.", "A gold brooch inlaid with jet and garnet.", "Huge ornately carved mahogany doors. Very heavy.", "A gilded and illuminated manuscript.", "A small box inlaid with mother of pearl.", "A matching pair of platinum rings. Each with a large pearl inset. They are worth 50gp each; or 100 gp for the set.", "The keystone of the entrance arch from a legendary temple destroyed in an ancient warandom. (50lb) – priceless to the right collectorandom.", "A 12x12ft, intricately patterned, thick, silk carpet. (200lb)", "An elven viol decorated with silver vines.", "A black onyx scepter with a head of a crow carved in the handle.", "A tapestry depicting the rise and fall of a recently conquered nearby city-state.", "A ceramic jug with glyphs of people teaching the spell ‘create food and water’. Can be used by wizards to copy into spell book.", "A see-through glass sword. The blade is made out of a clear blue glass while the handle is tinted blue.", "Ghostly and spectral remains that have been encased in a Crystal Ball. The ball glows faintly and has a swirling mist effect inside.", "A sheathe for a short sword long since forgotten. It is made with purple velvet wrapped owlbear leather, capped at the end by electrum. The inside has been smoothed considerably and lined with gelatinous cube remains. The effect of this is realized when drawing the sword, the sheathe generates zero sound whatsoeverandom. There is a carved wooden replica of the sword inside the sheathe, and all are contained within a see-through glass case wherein the sheathe lays horizontally.", "A headframe for a bed made with black ash logs. There are carved pictures of ravens decorating the headboard, and gold has been pressed into the carvings.", "A small gem encrusted crown, too small for most races, the crown is unique in that it has horsehair attached, allowing the crown to be worn as a wig.", "Iron ball and chain, there are carefully chiseled etchings in the chain and around the ball in dwarvish. If read, the etchings reveal a song about a criminal held in confinement for killing a noble, but her jailhouse was besieged by bandits for a yearandom. After the first verse, the faint chiseled etchings become deeper and clearer, telling of the dwarf’s temporary release and subsequent victory in combat of the besiegers alongside her jailers. The third and final verse is carved faintly and carefully again, detailing the dwarf continuing her life sentence until her death.", "An ivory tusk the length of an arm but carved with scenes from a battle long ago.", "A polished brass and copper clockwork toy of a small cottage, a farmer and their animals that moves when wound. The farmer chases a toy chicken with an axe.", "A scrimshaw pipe. When puffed on small skeletal animal smoke shapes rise out.", "A white porcelain chamber pot, the much-maligned last work of a great artist who went mad. The pot has the signature of the artist scrawled on it in a shaky hand.", "A painting that was started but not finished that depicts a beautiful landscape. It was started by a famous painter but unfortunately, he died halfway through finishing it. Parts of it are still sketched while others are fully painted.", "A tiny sundial made from a single piece of platinum.", "This ornate oak chair is both artsy AND functional. Sculpted by talented elven Craftsman as a wealthy dining set but have been split up due to warandom. Each chair depicts a different scene in a major war that happened thousands of years ago.", "A small, ornate hand-mirror, with decorative trim and a quote running along the edges that reads ‘Beauty is Diligence in Physical Form’.", "a painting with a mage shouting spells, it is clearly readable out of his mouth, but the letters become denser and denser until it’s only black paint.", "A portrait that makes a 3d bust illusion of a designated person. Requires a simple ritual to ‘take the picture’.", "A mirror that makes you look more attractive via illusion magic.", "A vase made from beautiful stone, carved with celestial figures around it, some marble inlays", "A silver circlet with a glowing stone in it, it can be used to cast light once per day", "An abstract art piece, not of any notable artist, but painted with specks of stones with permanent and colorful illumination.", "An ornate mantle clock that rings the hour with twelve separate melodies.", "A boldly colored quartz the size of a pigeon’s egg, etched and painted in such a way that when it is placed to one’s eye in the light, they see a clever but naughty image of a beautiful person in the nude.", "A wood bound codex filled illuminated with several hundred pages of highly colorful and anatomically difficult descriptions of sexual positions. The codex is sealed with a small brass chain. The text of the manuscript is in a language that is not common.", "A disk of clay with extremely fine etchings of semi-concentric lines that seem to spiral outwards from the center in tight, semi random wiggly spirals. It has been broken into three shards.", "A hat-stand made with ornate knobs of polished brass on the ends of the hooks. The knobs are animal heads in fine detail.", "A desktop ornament made of pink clear glass in the shape of a pig with a bright red glass apple in its mouth. When the pig is rubbed, it makes a magical oink noise.", "An ornate, decorative inkpot and penknife made of rare animal horn.", "A wire basket handled rapier of ornate design, with a fake ruby made of glass mounted in the pommel. The rapier is mounted to be a trophy on a wall. A small plaque reads, ‘Wrath’.", "A large globe showing the known world and a nested set of platonic solids, all made of brass. The entire contraption is over a meter across.", "A palm sized gelatinous cube containing a finely crafted model ship. The cube has been permanently suspended in animation with magic and is non-threatening.", "A painting of a flail snail enhanced by magic to project faint rainbow light from the shell of the flail snail.", "a handcrafted dreamcatcher adorned with werewolf teeth", "The mask of a cloud giant. The mask is pearl white and has light pink stripes.", "A sentient, immobile, carved basalt statue of a jellyfish, summoned to godhood by a cult of Koa-Toa", "Silver Body chains, worn by a high priestess Yuan-Ti.", "A mind flayers brain kept inside of a glass containerandom.", "A perfectly preserved molt of a Yuan-Ti Abomination. The molt is displayed on a large wooden platform.", "A necklace with a large pearl eye, around the eye are ten smaller pearl eyes branching off of the central eye. The necklace is gold and fashioned to depict a beholderandom.", "A small wood totem carved to resemble a werewolf, stolen from a cult of Malarandom.", "A clock in the image of an owlbear’s face. It is of masterwork gnomish quality. Every hour the owlbear opens its mouth and a -hoot hoot- sound emanates from the clock. At nighttime the eyes of the owlbear glow blood red.", "A gnomish tinkered hummingbird that fly’s in place for eternity.", "A palm sized jade turtle. While visibly impressive, most appraisers know it is of sub-par craftsmanship.", "A glass display with the first 100 gold coins minted by a nearby dwarven civilization.", "A display of a stone giants stone club. far too heavy to wield by medium sized creatures.", "A grey ooze that has been polymorphed into a throw rug. The ooze is unable to move across the floor on its own, however is constantly moving ‘within’ itself, giving the appearance of a swirling void.", "A palm sized carved stone replica of the Tomb of Horrors.", "A single Coatl feather, on a palm leaf.", "A candle made of red wax, in the image of a fire salamander", "A candle holder fashioned to resemble a fire mephit holding the candle. The candle holder is made of silverandom.", "The crown of a lizard king. The crown is made of gold and has images of lizardfolk fighting various fey creatures for control of a swamp.", "A perfectly preserved bone skull of a Sahuagin, on a corral wall mount", "The wrappings of a mummy inside a locked trunk.", "A small living carnivorous plant, inside of a notably larger iron cage.", "A carved golden sun, meant to mounted on a wall", "A stone tiled gameboard. the gameboard has stone figurines of adventurers fighting goblins in a dungeon.", "A painting of a ship sailing away from Waterdeep bay.", "A carved tusk of an unknown monster, depicting druids in the middle of a ritual", "An ornate, smooth orb of hardened tree sap (mixed with lavender dye.) It has the appearance of a round translucent ball (the size of a tennis ball in real life) with a dark purple hue and is often mistaken for an old family heirloom. Perhaps an Eboron spell wright believes it is her great grandmother’s spell casting focus, passed down for generations, or is a rather loud-mouthed, malicious constable found in his office every morning adoring his magnificent paper weight with an unusual amount of quiet glee?", "A singular wooden box, with 1-year worth of every spice in the world.", "A non-magical stone ‘official’ seal carved of three birds in flight with a blank spot where the buyer’s official crest can be added.", "Six ornately decorated candles with religious symbolism, and tapers (for lighting), in a small, smoked boxwood case of fine craftsmanship, with space for a seventh candle.", "A finely tanned, soft leather pouch filled with thirty-six small, polished hematite tiles about 2 cm across, inscribed with non-magical glyphs on both sides. Some of the tiles have different glyphs on opposing sides. The pouch has a leather drawstring.", "A birch and mahogany game-board approximately 30 centimeters across. The squares of the board are arrayed in a 9×9 pattern. A small set of two matching birch tables only 10 centimeters high accompany the board.", "A brass and glass hand-mirror with an intricate wirework for the handle. The wirework is of a bird in a cage.", "A polished brass telescoping spyglass, compass, octant, and slide rule set with precisely engraved markings and extreme precision. It comes in a velvet lined wooden case that has been treated with beeswax.", "A small chest for storing jewels in but made completely without nails. The outside of the chest has been lacquered red and inlaid with some very fine parquetry of a fruiting tree.", "A gilded oil lamp with ornate scrollwork cutouts of a warrior, and an evil sorcerer, meant to cast shadows on the wall in their shape.", "A fine glass lensed magnifying glass tied by a red silk ribbon to a codex filled with hundreds of pages of detailed illumination regarding the natural world."]
	
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
		p1 = ["Animal Control (250 gp)", "Clairaudience (250 gp)", "Clairvoyance (300 gp)", "Climbing (300 gp)", "Delusion", "Delusion", "Diminution (300 gp)", "Dragon Control (700 gp)", "Elixir of Health (350 gp)", "Elixir of Madness", "Elixir of Madness", "Elixir of Youth (500 gp)", "ESP (500 gp)", "Extra-healing (400 gp)", "Extra-healing (400 gp)", "Fire Breath (400 gp)", "Fire Resistance (250 gp)", "Flying (500 gp)", "Gaseous Form (300 gp)"]
		p2 = ["Giant Control (600 gp)","Giant Strength Warrior (550 gp)","Growth (250 gp)","Healing (200 gp)","Healing (200 gp)","Heroism Warrior (300 gp)","Human Control (500 gp)","Invisibility (250 gp)","Invulnerability Warrior (350 gp)","Levitation (250 gp)","Longevity (500 gp)","Oil of Acid Resistance (500 gp)","Oil of Disenchantment (750 gp)","Oil of Elemental Invulnerability (500 gp)","Oil of Etherealness (600 gp)","Oil of Fiery Burning (500 gp)","Oil of Fumbling","Oil of Impact (750 gp)","Oil of Slipperiness (400 gp)"]
		p3 = ["Oil of Timelessness (500 gp)","Philter of Glibness (500 gp)","Phliter of Love (200 gp)","Phliter of Persuasiveness (400 gp)","Phliter of Stammering and Stuttering","Plant Control (250 gp)","Poison","Poison","Polymorph Self (200 gp)","Rainbow Hues (200 gp)","Speed (200 gp)","Super-heroism Warrior (450 gp)","Super-heroism Warrior (450 gp)","Weet Water (200 gp)","Treasure Finding (600 gp)","Undead Control (700 gp)","Ventriloquism (200 gp)","Vitality (300 gp)","Water Breathing (400 gp)"]	
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
		num_spells = [1,1,1,1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
		wll = [1,1,1,1,1,2,1,2,1,2,1,1,1,1,1,3,1,2,4]
		wlu = [4,4,4,5,5,9,4,9,4,9,6,8,6,8,6,8,8,9,9]
		pll = [1,1,1,1,1,2,1,2,1,2,1,1,1,1,1,3,1,2,4]
		plu = [4,4,4,6,6,7,4,7,4,7,6,6,6,6,6,6,8,7,7]
	
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
			non_spell_scrolls = ["Map", \
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
			"Cursed"]
			sout += non_spell_scrolls[d20]
	
		return(sout)
	
	##############
	# Ring Picker
	def rings():
		rout = "\n> Ring of "
		d20 = random.randint(0,18)
		rings_low = ["Animal Friendship (1000 xp)",\
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
					"Protection (1000xp * level of protection)"]
	
		rings_high = ["Protection (1,000 xp * level of protection xp)", \
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
		"X-Ray Vision (4,000 xp)"]
	
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
		rods = ["Absorption Priest, Wizard (7,500 xp)", \
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
		"Terror (3,000 xp)"]
	
		rout += random.choice(rods)
		return(rout)
	
	#################
	# Staff Picker
	def staffs():
		stout = "\n> Staff of "
		staffs = ["Mace (1500 xp)",\
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
			"Woodlands Druid (8000 xp)"]
		stout += random.choice(staffs)
		return(stout)		
			
	################
	# Wand Picker
	def wands():
		wout = "\n> Wand of "
		wands = ["Conjuration (Wizard) (7,000 xp)", \
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
			"Wonder (6,000 xp)"]
		wout += random.choice(wands)
		return(wout)
	
	################
	# Misc Books and Tomes Picker
	def booksandtomes():
		bout = "\n> "
		l = ["Boccob’s Blessed Book (Wizard) (4,500 xp)", \
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
			"Vacuous Grimoire"]
		bout += random.choice(l)
		return(bout)
	
	################
	# Misc Jewels and Jewelry Picker
	def jewelry():
		jout = "\n> "
		l1 = ["Amulet of Inescapable Location", \
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
			"Necklace of Strangulation"]
		l2 = ["Pearl of Power (Wizard) (200 xp per level)", \
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
			"Talisman of Zagy (1,000 xp)"]
	
		if random.randint(1,2) == 1:
			jout += random.choice(l1)
		else:
			jout += random.choice(l2)
	
		return(jout)
	
	################
	# Misc Cloaks and Robes Picker
	def cloaks():
		rout = "\n> "
		l = ["Cloak of Arachnida (3,000 xp)", \
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
			"Robe of Vermin (Wizard)"]
		rout += random.choice(l)
		return(rout)
	
	################
	# Misc Boots and Gloves Picker
	def boots():
		bout = "\n> "
		l = ["Boots of Dancing", \
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
			"Slippers of Spider Climbing (1,000 xp)"]
		bout += random.choice(l)
		return(bout)
	
	################
	# Misc Girdles and Helms Picker
	def girdles():
		out = "\n> "
		l =["Girdle of Dwarvenkind (3,500 xp)", \
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
			"Helm of Underwater Action (1,000 xp)"]
		out += random.choice(l)
		return(out)
	
	################
	# Misc Bags and Bottles Picker
	def bags():
		out = "\n> "
		l = ["Alchemy Jug (3,000 xp)", \
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
			"Pouch of Accessibility 1,500"]
		out += random.choice(l)
		return(out)
	
	################
	# Misc Dusts and Stones Picker
	def dusts():
		out = "\n> "
		l = ["Candle of Invocation (Priest) (1000 xp)", \
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
			"Universal Solvent (1000 xp)"]
		out += random.choice(l)
		return(out)
	
	################
	# Misc Household Items and Tools Picker
	def tools():
		out = "\n> "
		l = ["Brazier Commanding Fire Elementals (Wizard) (4000 xp)", \
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
			"Spade of Colossal Excavation (Warrior) (1000 xp)"]
		out += random.choice(l)
		return(out)
	
	################
	# Misc Musical Instruments Picker
	def instruements():
		out = "\n> "
		l = ["Chime of Interruption (2000 xp)", \
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
			"Pipes of the Sewers (2000 xp)"]
		out += random.choice(l)
		return(out)
	
	
	################
	# Misc Weird Stuff Picker
	def weird():
		out = "\n> "
		l = ["Apparatus of Kwalish (8000 xp)", \
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
			"Wings of Flying (750 xp)"]
		out += random.choice(l)
		return(out)
	
	################
	# Armor Picker
	def armors():
		out = "\n> Armor: "
		mod = ""
	
		# get type of armor
		armors = ['Banded mail', \
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
				  "Special"]
		a = random.choice(armors)
		
		# determine if special
		special_armors = ["Armor of Command (+1000 xp)", "Armor of Blending (+500 xp)", "Armor of Missile Attraction", "Armor of Rage", "Elven Chain Mail (+1000 xp)", "Plat Mail of Etherealness (5000 xp)", "Plate Mail of Fear (4000 xp)", "Plate Mail of Vulnerability", "Shield large, -1 AC, -4 AC vs missiles (400 xp)", "Shield +1 AC, Missile Attractor"]
		if a == "Special":
			a = random.choice(special_armors)
			out += a
		
		# determine mod
		else:
			d20 = random.randint(0,19)
			xps = [0, 0, 500, 500, 500, 500, 500, 500, 500, 500, 500, 1000, 1000, 1000, 1000, 1500, 1500, 1500, 2000, 2000, 3000]
			mods =[1, 1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   -2,   -2,   -2,   -2,   -3,   -3,   -3,   -4,   -4,   -5]
	
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
			sw1 = ["Arrow of Direction (2500 xp)", \
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
					"Hammer of Thunderbolts (2500 xp)"]
			sw2 = ["Hornblade", \
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
					"Trident of Yearning"]
			sw3 = ["Sun Blade (3000 xp)", \
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
					"Sword +2, Giant Slayer (900 xp)"]
			sw4 = ["Sword +2 Nine Lives Stealer (1600 xp)", \
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
					"Sword Vorpal Weapon (10000 xp)"]
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
	
	
	print(" == Loot == ")
	print(o)
	print("\n")


while True:
	main()
