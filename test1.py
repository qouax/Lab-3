try: 
	import sim
except:
	print('error... could not import sim.py')
	print('Make sure sim.py is located in the same folder as this')
sim.simxFinish(-1)
clientID=sim.simxStart('10.242.0.105',19999,True,True,5000,5)
if clientID!=-1:
	print ('Pass')
	sim.simxAddStatusbarMessage(clientID,'Pass',sim.simx_opmode_oneshot)
	sim.simxGetPingTime(clientID)
	sim.simxFinish(clientID)
else:
	print ('Fail')
