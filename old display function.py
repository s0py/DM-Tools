
# def display(rain,wind_max,day,weekday,month,monthday,\
# 	 hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
# 	 wind_low,wind_missile,wind_melee,wind_move,viz_day,\
# 	 viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season):
#def display(rain,wind_max,day,weekday,month,monthday,\
#	hi,lo,humiditymod,wind,winddir,eff_hi,eff_lo,spec,\
#	wind_low,wind_missile,wind_melee,wind_move,viz_day,\
#	viz_twi,viz_moon,viz_dark,wilderness,climate,terrain,season,food_list):
#	
#	dawn, dusk, dl = daylight(day,climate)
#
#	for i in range(0,25-len(rain)):
#		rain +=" "
#	for i in range(0,4-len(eff_hi)):
#		eff_hi = " " + eff_hi
#	for i in range(0,4-len(eff_lo)):
#		eff_lo = " " + eff_lo
#	for i in range(0,25-len(spec)):
#		spec += " "
#	for i in range(0,4-len(hi)):
#		hi = " " + hi
#	for i in range(0,4-len(lo)):
#		lo = " " + lo
#	if len(monthday) < 2:
#		monthday = " " + monthday
#	for i in range(0,13-len(month)):
#		month += " "
#	for i in range(0,4-len(day)):
#		day = " " + day
#	viz_day += " yds"
#	viz_twi += " yds"
#	viz_moon += " yds"
#	viz_dark += " yds"
#	for i in range(0,10-len(viz_day)):
#		viz_day += " "
#	for i in range(0,10-len(viz_twi)):
#		viz_twi += " "
#	for i in range(0,10-len(viz_moon)):
#		viz_moon += " "
#	for i in range(0,10-len(viz_dark)):
#		viz_dark += " "
#	wind_max += " mph"
#	for i in range(0,11-len(wind_max)):
#		wind_max += " "
#	for i in range(0,20-len(winddir)):
#		winddir += " "
#	for i in range(0,11-len(wind_missile)):
#		wind_missile += " "
#	for i in range(0,11-len(wind_melee)):
#		wind_melee += " "
#	for i in range(0,11-len(wind_move)):
#		wind_move += " "
#	humiditymod += "%"
#	for i in range(0,4-len(humiditymod)):
#		humiditymod += " "
#
#	for i in range(0,31-len(wilderness[0][1])):
#		wilderness[0][1] += " "
#	for i in range(0,31-len(wilderness[1][0])):
#		wilderness[1][0] += " "
#	for i in range(0,31-len(wilderness[1][1])):
#		wilderness[1][1] += " "
#	for i in range(0,31-len(wilderness[1][2])):
#		wilderness[1][2] += " "
#	for i in range(0,31-len(wilderness[1][3])):
#		wilderness[1][3] += " "
#	for i in range(0,18-len(wilderness[2][1])):
#		wilderness[2][1] += " "
#	for i in range(0,18-len(wilderness[2][2])):
#		wilderness[2][2] += " "
#	for i in range(0,18-len(wilderness[2][3])):
#		wilderness[2][3] += " "
#	for i in range(0,3-len(wilderness[3][0])):
#		wilderness[3][0] += " "
#	for i in range(0,18-len(wilderness[3][1])):
#		wilderness[3][1] += " "
#	for i in range(0,18-len(wilderness[5][1])):
#		wilderness[5][1] += " "
#	for i in range(0,18-len(wilderness[5][2])):
#		wilderness[5][2] += " "
#	for i in range(0,13-len(wilderness[4])):
#		wilderness[4] += " "
#	for i in range(0,24-len(wilderness[6])):
#		wilderness[6] += " "
#	for i in range(0,10-len(climate)):
#		climate += " "
#	for i in range(0,10-len(terrain)):
#		terrain += " "
#	for i in range(0,10-len(season)):
#		season += " "
#	for i in range(0,4-len(dl)):
#		dl = " " + dl
#
#	# deal with the stupid way we are displaying the food
#	fl1_n =  str(food_list[0][0])
#	fl1_s =  str(food_list[0][-1])
#	fl2_n =  str(food_list[1][0])
#	fl2_s =  str(food_list[1][-1])
#	fl3_n =  str(food_list[2][0])
#	fl3_s =  str(food_list[2][-1])
#	fl4_n =  str(food_list[3][0])
#	fl4_s =  str(food_list[3][-1])
#	fl5_n =  str(food_list[4][0])
#	fl5_s =  str(food_list[4][-1])
#	fl6_n =  str(food_list[5][0])
#	fl6_s =  str(food_list[5][-1])
#	fl7_n =  str(food_list[6][0])
#	fl7_s =  str(food_list[6][-1])
#	fl8_n =  str(food_list[7][0])
#	fl8_s =  str(food_list[7][-1])
#	fl9_n =  str(food_list[8][0])
#	fl9_s =  str(food_list[8][-1])
#	fl10_n = str(food_list[9][0])
#	fl10_s = str(food_list[9][-1])
#	fl11_n = str(food_list[10][0])
#	fl11_s = str(food_list[10][-1])
#	fl12_n = str(food_list[11][0])
#	fl12_s = str(food_list[11][-1])
#
#	for i in range(0,16-len(fl1_n)):
#		fl1_n += " "
#	for i in range(0,3-len(fl1_s)):
#		fl1_s += " "
#	for i in range(0,16-len(fl2_n)):
#		fl2_n += " "
#	for i in range(0,3-len(fl2_s)):
#		fl2_s += " "
#	for i in range(0,16-len(fl3_n)):
#		fl3_n += " "
#	for i in range(0,3-len(fl3_s)):
#		fl3_s += " "
#	for i in range(0,16-len(fl4_n)):
#		fl4_n += " "
#	for i in range(0,3-len(fl4_s)):
#		fl4_s += " "
#	for i in range(0,16-len(fl5_n)):
#		fl5_n += " "
#	for i in range(0,3-len(fl5_s)):
#		fl5_s += " "
#	for i in range(0,16-len(fl6_n)):
#		fl6_n += " "
#	for i in range(0,3-len(fl6_s)):
#		fl6_s += " "
#	for i in range(0,16-len(fl7_n)):
#		fl7_n += " "
#	for i in range(0,3-len(fl7_s)):
#		fl7_s += " "
#	for i in range(0,16-len(fl8_n)):
#		fl8_n += " "
#	for i in range(0,3-len(fl8_s)):
#		fl8_s += " "
#	for i in range(0,16-len(fl9_n)):
#		fl9_n += " "
#	for i in range(0,3-len(fl9_s)):
#		fl9_s += " "
#	for i in range(0,16-len(fl10_n)):
#		fl10_n += " "
#	for i in range(0,3-len(fl10_s)):
#		fl10_s += " "
#	for i in range(0,16-len(fl11_n)):
#		fl11_n += " "
#	for i in range(0,3-len(fl11_s)):
#		fl11_s += " "
#	for i in range(0,16-len(fl12_n)):
#		fl12_n += " "
#	for i in range(0,3-len(fl12_s)):
#		fl12_s += " "
#
#
#	os.system('cls')
#	print('═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
#	print('this program is reading from : {}'.format(file))
#	print('')
#	print('                                             Current Conditions')
#	print('┌───────────────────────────┬───────────┐ ┌──────────────────────┐ ┌─────────────────────────────────┐ ┌─────────────────────────┐')	# 1
#	print('│       weather   hum: {} │   hi   lo │ │         wind         │ │     surrounding wilderness      │ │          food           │'.format(humiditymod))	# 2
#	print('├───────────────────────────┼───────────┤ ├──────────────────────┤ ├─────────────────────────────────┤ ├─────────────────────────┤')	# 3
#	print('│ {} │ {} {} │ │          {} │ │ hunt                            │ │  1 {} {} │'.format(rain,eff_hi,eff_lo,wind_max,fl1_s,fl1_n))	# 4
#	print('│ {} │ {} {} │ │ {} │ │ {} │ │  2 {} {} │'.format(spec,hi,lo,winddir,wilderness[0][1],fl2_s,fl2_n))	# 5
#	print('└───────────────────────────┴───────────┘ │                      │ │                                 │ │  3 {} {} │'.format(fl3_s,fl3_n))	# 6
#	print('            ┌───────────────────────────┐ │ missiles {} │ │ fish                            │ │  4 {} {} │'.format(wind_missile,fl4_s,fl4_n))	# 7
#	print(' {} │ {} {}  (d {})│ │    melee {} │ │ {} │ │  5 {} {} │'.format(climate,monthday,month,day,wind_melee,wilderness[1][0],fl5_s,fl5_n))	# 8
#	print(' {} ├───────────────────────────┤ │     move {} │ │ {} │ │  6 {} {} │'.format(terrain,wind_move,wilderness[1][1],fl6_s,fl6_n))	# 9
#	print(' {} │            day {} │ └──────────────────────┘ │ {} │ │  7 {} {} │'.format(season,viz_day,wilderness[1][2],fl7_s,fl7_n))	# 10
#	print('            │       twilight {} │ ┌──────────────────────┐ │ {} │ │  8 {} {} │'.format(viz_twi,wilderness[1][3],fl8_s,fl8_n))		# 11
#	print(' dawn {} │      moonlight {} │ │     morale checks    │ │                                 │ │  9 {} {} │'.format(dawn,viz_moon,fl9_s,fl9_n))		# 12
#	print(' dusk {} │           dark {} │ ├──────────────────────┤ │ forage                          │ │ 10 {} {} │'.format(dusk,viz_dark,fl10_s,fl10_n))		# 13
#	print(' ({} h)   └───────────────────────────┘ │ surprised            │ │      found : {} │ │ 11 {} {} │'.format(dl,wilderness[2][1],fl11_s,fl11_n))		# 14
#	print('           ┌────────────────────────────┐ │ superior force       │ │ prof found : {} │ │ 12 {} {} │'.format(wilderness[2][2],fl12_s,fl12_n))
#	print('           │      water min (pints)     │ │ ally slain by magic  │ │    problem : {} │ └─────────────────────────┘'.format(wilderness[2][3]))
#	print('           ├────────────────────────────┤ │ 1/4 group fallen     │ │                                 │')
#	print('           │          <50  <70  <90   + │ │ 1/2 group fallen     │ │ water : {}, {} │'.format(wilderness[3][0],wilderness[3][1]))
#	print('           │ inactive   5    6    7   8 │ │ " " " & ally falls   │ │                                 │')
#	print('           │    light   6    7    8  10 │ │ tempted (bribe, &c)  │ │ medicinal plant                 │')
#	print('           │ moderate   8    9   10  12 │ │ covering rear guard  │ │      found : {} │'.format(wilderness[5][1]))
#	print('           │    heavy   9   10   12  16 │ │ use magic charge     │ │ prof found : {} │'.format(wilderness[5][2]))
#	print('           └────────────────────────────┘ │ surrounded           │ │                                 │')
#	print('                                          └──────────────────────┘ │ natural shelter : {} │'.format(wilderness[4]))
#	print('                                                                   │ fuel : {} │'.format(wilderness[6]))
#	print('                                                                   └─────────────────────────────────┘')
#	print('')
