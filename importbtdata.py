import bluetooth
 
bd_addr = "" #This will be the address from the arduinos
port = 1 
sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
sock.connect((bd_addr,port))
 
data = ""
while 1:
	try:
		data += sock.recv(1024)
		data_end = data.find('\n') #add a terminator to the string in the aduino code, so only prints the received data in python once terminator has been received
		if data_end != -1:
			rec = data[:data_end]
			print data
			data = data[data_end+1:]
	except KeyboardInterrupt:
		break
sock.close()
