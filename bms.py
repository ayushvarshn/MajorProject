import time
import os
from os import system, name
import random
import csv
cycle = 0
curr_sens = 0.185
vref=5

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')


def get(x):
	if (int(x)==0):
		input=[1,random.uniform(0.5,0.8)]
	else:
		input=[1,random.uniform(0.2,0.5)]
	return input

def measure(x):
	if (int(x)==0):
		ch=get(0)
	else:
		ch=get(1)
	print('\n Actual output from ADC is || ','%.2f'%ch[0],'|','%.2f'%ch[1],'||\n')
	voltage = 0
	for i in range(6):
		voltage = voltage + ch[0]*vref
	voltage = voltage/6
	current = 0
	for i in range(6):
		current = current + ((ch[1]-0.5)*vref)/curr_sens
	current = current/6
	current=round(current,2)
	#print('\n \n V=',voltage,'I=',current)
	return voltage, current

def fetch(x):
	return float(data[x][1]), -float(data[x][0])
	

def main():
	clear = lambda: os.system('cls')
	ampHours = 0
	aim=1
	meanI=0
	meanV=0
	count=0
	cu=0
	capacity=1.1
	c=0
	soc=1
	global cycle
	cycle = 0
	while True:
		count+=1
		t1 = time.perf_counter()
		charge_cycles = (aim-1)+ ampHours/capacity
		soc=round((capacity-cu)/capacity,3)
		cycle=charge_cycles
		cycle=round(cycle,3)
		if (soc > 1):
			c=0
			soc=1
			cu=0
		if(cycle>aim):
			cycle=aim
			aim+=1
			ampHours=0
			c=1
			screen_clear()
			print("\n \n \n \t \t BATTERY HAS DISCHARGED COMPLETELY")
			print("\t \t Please give some charging current")
			time.sleep(2)
		screen_clear()
		print('\t \t BATTERY MONITORING SYSTEM')
		print('\t \t  Alka, Aman, Anu, Ayush \n ')
		print('\n')
		print('Maximum Capacity :%.2f'%capacity,'\n')
		print('\t Cycles=',cycle)
		print('\t SOC=',round(soc*100, 2), '%')
		vol, curr = measure(c)
		#vol, curr = fetch(count)
		print('\n')
		
		if (soc<=0 and curr > 0):
			curr = 0
		if (soc>=1 and curr < 0):
			curr = 0
		print("Voltage = ", round(vol, 2), " | Current = ", round(curr, 2))
		#capacity= predict_max_cap(vol,cycle)
		time.sleep(3)
		t2 = time.perf_counter()
		delta_t = (t2-t1)*10
		if (curr > 0): #Discharging
			ampHours = ampHours + (curr*delta_t/3600)
		else:
			ampHours = ampHours
		cu = cu + (curr*delta_t/3600)
		
		
global data

data=[]
with open('data.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	
	for line in csv_reader:
		data.append(line)
		

screen_clear()
print('Welcome')
time.sleep(2)
try:
	main()
except KeyboardInterrupt:
	screen_clear()
	print('\n')
	print("Exiting....")
	print('\n')
	time.sleep(1)
	screen_clear()

