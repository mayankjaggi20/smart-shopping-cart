import serial
import sqlite3
conn = sqlite3.connect("super.db")
c = conn.cursor()
rfidlist=[]
while(True):
	def read_rfid ():
		ser = serial.Serial ("/dev/ttyAMA0")
#Open named port
	ser.baudrate = 9600
#Set baud rate to 9600
	data = ser.read(12)
#Read 12 characters from serial port to data
	ser.close ()
#Close port
	return data
#Return data
	id = read_rfid ()

#Function call

	a = id
	#a=input()
	if a in rfidlist:
		rfidlist.remove(a)
	else:
		rfidlist.append(a)
	print(rfidlist)

	try:
		num0=rfidlist[0]
	except IndexError:
		num0=0

	try:
		num1=rfidlist[1]
	except IndexError:
		num1=0

	try:
		num2=rfidlist[2]
	except IndexError:
		num2=0

	c.execute("SELECT objname, price, count(*) FROM object where rfid in (?,?,?) group by objid;", (num0,num1,num2,))

	pr = c.fetchall()
	print(pr)

	b = 0
	if b in rfidlist:
		rfidlist.remove(b)
	if b in rfidlist:
		rfidlist.remove(b)
	if b in rfidlist:
		rfidlist.remove(b)

conn.close()