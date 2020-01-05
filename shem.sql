DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS passenger;
DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS flightHistory;

CREATE TABLE IF NOT EXISTS passenger (
	cnic VARCHAR(255) PRIMARY KEY, 
	fname VARCHAR(255),
	lname VARCHAR(255),
 	address VARCHAR(255), 
 	phone VARCHAR(255),
 	nationality CHAR(255));

CREATE TABLE IF NOT EXISTS flightHistory (
	flight_history_ID INT AUTO_INCREMENT PRIMARY KEY,
	flight_id VARCHAR(225),
	passenger_id VARCHAR(255));

CREATE TABLE IF NOT EXISTS flight (
	flight_id VARCHAR(225) PRIMARY KEY,
	departure_airport VARCHAR(255),
	arrival_airport VARCHAR(255),
	arrival_time VARCHAR(255),
	departure_time VARCHAR(255),
	fare INT, 
	airplane CHAR(255));

CREATE TABLE IF NOT EXISTS ticket (
	ticket_id INT AUTO_INCREMENT PRIMARY KEY,
	flight_id VARCHAR(225),
	passenger_id VARCHAR(255),
	FOREIGN KEY (flight_id) REFERENCES flight(flight_id),
	FOREIGN KEY (passenger_id) REFERENCES passenger(cnic));