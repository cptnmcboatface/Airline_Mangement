# test.py
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hamzah123",
  database="mydatabase"
)

mycursor = mydb.cursor()


# CREATE TABLE IF NOT EXISTS passenger (
# 	cnic VARCHAR(255) PRIMARY KEY, 
# 	fname VARCHAR(255),
# 	lname VARCHAR(255),
#  	address VARCHAR(255), 
#  	phone VARCHAR(255),
#  	nationality CHAR(255));
def updateRecord():
	os.system("clear")
	print("Update PASSENGER Cred: ")
	cnic = input("Enter Passenger CNIC: ")

	mycursor.execute("SELECT * FROM passenger where cnic = "+cnic)
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	print("\n\n")
	Fname = input("Enter First Name: ")
	Lname = input("Enter Last Name: ")
	add = input("Enter Address: ")
	phoneNumber = input("Enter Phone No. : ")
	nationality = input("Enter Nationality: ")

	sql = "UPDATE passenger SET fname = %s, lname=%s,add=%s ,phone =%s ,nationality =%s WHERE cnic = %s"
	val = (Fname,Lname, phoneNumber, nationality,cnic)
	mycursor.execute(sql,val)
	mydb.commit()
	print("DONE!")
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")

def getFlightHistory():
	os.system("clear")
	print("FLIGHT RECORD: ")
	cnic = input("ENTER Passenger CNIC: ")
	mycursor.execute("SELECT * from flightHistory WHERE passenger_id = "+ cnic)
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")

def cancelFlight():
	os.system("clear")
	print("CANCEL TICKET")
	cnic = input("Enter CNIC: ")
	mycursor.execute("SELECT * from ticket WHERE passenger_id = "+ cnic)
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	flight = input("ENTER FLIGHT ID: ")
	sql = "DELETE FROM ticket WHERE passenger_id = %s AND flight_id = %s"
	val = (cnic, flight)
	mycursor.execute(sql, val)
	mydb.commit()

	print("TICKET RECORD DELETED!")

	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")


def cheapestFlight():
	os.system("clear")
	print("CHEAPEST FLIGHT: ")
	dep_air = input("ENTER DEPARTURE AIRPORT: ")
	arr_air = input("ENTER ARRIVAL AIRPORT: ")
	sql = "SELECT * from flight WHERE arrival_airport = %s AND departure_airport = %s ORDER BY fare limit 1"
	val = (arr_air, dep_air)
	mycursor.execute(sql, val)

	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")

def generateTicket():
	os.system("clear")
	print("AVAILABLE FLIGHTS: ")
	
	mycursor.execute("SELECT * FROM flight")
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	flight = input("ENTER FLIGHT: ")
	cnic = input("Enter CNIC: ")
	val = (flight, cnic)
	mycursor.execute("INSERT INTO ticket(flight_id, passenger_id) values"+str(val))
	mydb.commit()

	mycursor.execute("INSERT INTO flightHistory(flight_id, passenger_id) values"+str(val))
	mydb.commit()

	print("TICKET GENERATED!")
	input("Press Any Key To Continue...")
	os.system("clear")
# CREATE TABLE IF NOT EXISTS ticket (
# 	ticket_id INT AUTO_INCREMENT PRIMARY KEY,
# 	flight_id VARCHAR(225),
# 	passenger_id VARCHAR(255),



def getFlightRecord():
	os.system("clear")
	print("GET FLIGHT RECORD\n")
	dep_air = input("ENTER DEPARTURE AIRPORT: ")
	arr_air = input("ENTER ARRIVAL AIRPORT: ")
	sql = "SELECT * FROM flight where departure_airport = %s AND arrival_airport = %s" 
	val = (dep_air,arr_air)

	mycursor.execute(sql, val)

	myresult = mycursor.fetchall()
	print("HERE ARE ALL THE FLIGHTS: ")
	for x in myresult:
	  print(x)
	input("Press Any Key To Continue...")
	os.system("clear")

def createRecord():
	# insert into passenger values("36302", "areeb1","qamar", "lums","0332472", "pak1");
	os.system("clear")	
	print("ENTER PASSENGER DATA")
	cnic = input("Enter CNIC: ")
	Fname = input("Enter First Name: ")
	Lname = input("Enter Last Name: ")
	add = input("Enter Address: ")
	phoneNumber = input("Enter Phone No. : ")
	nationality = input("Enter Nationality: ")

	sql = "INSERT INTO passenger (cnic, fname,lname,address,phone,nationality) VALUES (%s, %s, %s, %s, %s, %s)"
	val = (cnic, Fname,Lname, add,phoneNumber, nationality)
	mycursor.execute(sql,val)
	mydb.commit()
	print("PASSENGER LOGGED!")
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")	

def createFlight():
	os.system("clear")
	print("CREATE FLIGHT!")
	flight_id = input("ENTER FLIGHT ID: ")
	arrival_airport = input("ENTER ARRIVAL AIRPORT: ")
	departure_airport = input("ENTER DEPARTURE AIRPORT: ")
	arrival_time = input("ENTER ARRIVAL TIME: ")
	departure_time = input("ENTER DEPARTURE TIME: ")
	fare = int(input("Enter Fare: "))
	airplane = input("Enter Airplane: ")

	sql = "INSERT INTO flight (flight_id, arrival_airport,departure_airport,arrival_time,departure_time,fare,airplane) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	val = (flight_id, arrival_airport,departure_airport,arrival_time,departure_time,fare,airplane)
	mycursor.execute(sql,val)
	mydb.commit()
	print("FLIGHT LOGGED!")
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")	



def getAirportRecord():
	os.system("clear")
	print("FLIGHTS ON AIRPORT")
	airport = input("ENTER AIRPORT: ")
	sql = "SELECT * from flight where arrival_airport = %s OR departure_airport = %s"
	val = (airport, airport)

	mycursor.execute(sql, val)
	myresult = mycursor.fetchall()
	print("HERE ARE ALL THE FLIGHTS: ")
	for x in myresult:
	  print(x)
	input("Press Any Key To Continue...")
	os.system("clear")

def updateRecord():
	os.system("clear")
	print("Update FLIGHT RECORD: ")
	flight_id = input("Enter FLIGHT ID: ")
	
	mycursor.execute("SELECT * FROM flight where flight_id = \""+str(flight_id)+"\"")
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)

	print("\n\n")

	arrival_airport = input("ENTER ARRIVAL AIRPORT: ")
	departure_airport = input("ENTER DEPARTURE AIRPORT: ")
	arrival_time = input("ENTER ARRIVAL TIME: ")
	departure_time = input("ENTER DEPARTURE TIME: ")
	fare = int(input("Enter Fare: "))
	airplane = input("Enter Airplane: ")

	sql = "UPDATE flight SET arrival_airport = %s, departure_airport=%s,arrival_time=%s ,departure_time =%s ,fare =%s,airplane = %s WHERE flight_id = %s"
	val = (arrival_airport,departure_airport,arrival_time,departure_time,fare,airplane,flight_id)
	mycursor.execute(sql,val)
	mydb.commit()
	print("DONE!")
	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")

def cancelFlight():
	os.system("clear")
	print("CANCEL FLIGHT")
	flight_id = input("Enter FLIGHT ID: ")
	
	sql = 'DELETE FROM flight WHERE flight_id = "'+flight_id+'"'

	mycursor.execute(sql)

	mydb.commit()

	print("FLIGHT RECORD DELETED!")

	input("PRESS ANY KEY TO CONTINUE")
	os.system("clear")

def adminScreen():
	os.system('clear')
	while(1):
		print("1. GET FLIGHTS OF DAY\n")
		print("2. CREATE FLIGHT\n")
		print("3. UPDATE FLIGHT\n")
		print("4. CANCEL FLIGHT\n")
		selection = input('\nInput: ')
		if(selection =='1'):
			getAirportRecord()
		if(selection =='2'):
			createFlight()
		if(selection =='3'):
			updateRecord()
		if(selection =='4'):
			cancelFlight()




def receptionistScreen():
	os.system('clear')
	while(1):
		print("WELCOME RECEPTIONIST")
		print("1. Create Record\n")
		print("2. Update Details\n")
		print("3. Get Flight Record\n")
		print("4. Generate Flight Record\n")
		print("5. GET Cheapest Flight\n")
		print("6. GET Flight Record Passenger\n")
		print("7. Cancel Flight\n")
		selection = input("\nINPUT:")
		if selection == "1":
			createRecord()
		elif selection == "2":
			updateRecord()
		elif selection == "3":
			getFlightRecord()
		elif selection == "4":
			generateTicket()
		elif selection == "5":		
			cheapestFlight()
		elif selection == "6":
			getFlightHistory()
		elif selection == "7":
			cancelFlight()	


def receptionCredential():
	id = "areb"
	password = "123"
	os.system('clear')
	# id = input("ID: ")
	# password = input("PASSWORD: ")
	while(1):
		if id=="areb" and password == "123":
			receptionistScreen();
			break;
		else:
			print("INCORRECT CREDENTIALS TRY AGAIN")

def adminCredential():
	id = "areb"
	password = "123"
	os.system('clear')
	# id = input("ID: ")
	# password = input("PASSWORD: ")
	while(1):
		if id=="areb" and password == "123":
			adminScreen()
			break;
		else:
			print("INCORRECT CREDENTIALS TRY AGAIN")


def startScreen():
	print("WELCOME!\n")
	print("1: LOGIN AS ADMIN")
	print("2: LOGIN AS RECEPTIONIST")
	selection = (input("INPUT: "))
	if(selection ==  "2"):
		receptionCredential()
	else:
		adminCredential()
		



def main():
	global mydb,mycursor

	fhandle = open("shem.sql")
	script = fhandle.read()
	records = mycursor.execute(script,multi = True)
	for row in records:
		print(row)
	fhandle = open("pop.sql")
	populate = fhandle.read()
	result = mycursor.execute(populate,multi = True)	
	for row in result:
		print (row)
	mydb.commit()

	startScreen()
main()