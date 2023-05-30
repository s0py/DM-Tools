how to use it

1. the files it needs
it's going to read in some files. the main file that you'll need to provide it is the weather file. 
this can be generated using the 2weather.py but there is on already provided for you for each type of 
climate (arctic, subarctic, temperate, subtropical, tropical) and terrain (desert, forest, hill, 
mountain, plains, swamp, coast).

the other files it needs are the plants by climate, terrain, and season. these are taken specifically
from a text called "What Can Be Bought" which is freely available online.

when you run the program it will ask you what weather file you want to open. if you don't specify
one there is a default one that will be loaded.

2. what all the boxes tell you
most of the information it is going to tell you is based on the 1e Wilderness Survival Guide and
the various tables and rules it lays out. This tool is not a replacement for that text. this tool
just does all the annoying dice rolling and other boring bits for you so that you can reference and
use then as you need. 

at the top it tells you what file it's reading from
then it tells you the weather.
the first line under weather tells you the base weather and the one below tells you if there is
any special weather. you'll have to look up the specifics of what this special weather means in
the Wilderness Survival Guide. 
to the right are the high and low temeprates for the day. the top numbers are the effective temp-
eratures that take into account wind. this is what a character would feel (consider this the
"feels-like" temperatuer) and is in degrees Fahrenheit. the number below is the actual temperature.

To the right of this is the wind. the first line is the speed in mph. this is the maximum any gust
will be on a given day tho typically the windspeed is less than half this value.
below that is the direction the wind is coming from ("prevailing" means the direction the wind
typically comes from for that area)
below that are three rows detailing the modifiers to ranged weapons (in old dnd they are called
missile weapons), melee weapons, and movement against the wind. usually these are blank but a
full guide to reading them is in the Wilderness Survival Guide.

To the right of that is a box detailing the "Surrounding Wilderness".
This box is dependent on the climate, terrain, and season.
the first line, "hunt" tells you what a party spending 2 turns hunting will come across and how
far away they will be. there are full rules on how hunting encoutners work in the WSG.
below this is the results of spending 1 hour fishing. fishing with a net will increase this by 50%.
the numbers are determined by dice rolls and depend on time of day and how good a fishing spot it
is. these numbers are the numbers of fish which are caught. ignore negative numbers.

below this are the results of someone attempting to forage. the first line is whether someone will
find enough edible food for a single ration (2 lbs)., the next line is whether someone with the
foraging or gathering proficiency will find edible food (someone with the proficiency always finds
2 full rations or 4 lbs). the next line is whether there are any issues with the food such as it
being inedible, poisonous, rancid, etc.

below that is whether there is water in the area and followed by a comma is the condition of it

below that is whether medicinal plants can be found and then whether someone with the appropriate
proficiency could find them

lastly is whether this area has a natural shelter and whether there is enough fuel to last the night
to feed a fire.


going back all the way to the left is the current settings for, in order, climate, terrain, and
season. these may not match those of the weather file you imported. these are used to determine
many things in the program and all of the surrounding wilderness info so adjust them.

below this are the times of sunrise and sunset and how many total hours of daylight there are.
this is determined by the month and climate.

to the right is a calendar displaying the day of the month, the name of the month, and how many
total days into the weather spreadsheet you are. the calendar is a 360 day calendar with 12 months
and each month has exactly 30 days. the first day of the year is 1 Springmoon and is the first day
of spring.

below this are the distances which a human-size creature can be seen. this number is doubled for
large creaturs and halved for small creatures.

below this table is the minimum water needed for a human given the amount of activity and their
effective temperature. their personal effective temperature could vary based on clothing so this
is not simply a repurposing of the hi and lo temp section of the weather box.

to the right is a simple box detailing when is an appropriate time to make a morale check for 
enemies and NPCs. NEVER MAKE A MORALE CHECK FOR A PLAYER.


3. commands
the way you interact with this program is thru commands. they are one or two-letter commands and
are displayed at the bottom of the screen. to run a command, type it and then hit enter. if a 
command is not recognized it will simply refresh.

the commands are:

d - it will ask for a specific day you want to go to. type in the day number.
1 - typing any number will advance the calendar by that many days. negative numbers go backwards.
r - this is used mainly for testing; it sends you to a random day
m - this starts the morale check program
l - this rerolls all the information in the "surrounding wilderness" box and is used to indicate you
    are in a "new location" with the same climate, terrain, season, etc.
s - this is how you change the location paramters: climate, terrain, and season
p - this shows a table of all the plants which are available in this combination of climate, terrain,
    and season. if there are too many plants to display at one, the table is broken up into multi
    ple tables
i - this opens the initiative rolling program (adnd 2e)
sd - this opens up a program to modify prices of goods based on various events

MORALE PROGRAM
a list is brought up which shows all 26 ways in which a morale check can be modified in accordance
with the 2e dungeon master's guide. simply type the letters of all the modifiers and then hit enter.
the program will roll the dice and apply the modifiers and also report the total modifiers and the
result of the dice roll

INITIATIVE
this bring sup the initiative program. there is a number corresponding to all the modifiers of
initiative in accordance with the adnd 2e dungeon master's guide. simply enter the numbers
of the modifiers all in one line and press enter to roll initiative.

MARKET FORCES
this program will produce a table of how much to modify the price of vairous qualities of product
based on things which could disrupt a market. enter the letters of all the appropriate modifiers
and the program will ask you additional information.