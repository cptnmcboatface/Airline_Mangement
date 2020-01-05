delete  from flight;
delete from passenger;
insert into flight values("UK301", "LHR", "KHI", "08:00", "12:00", 135000, "ANJ-414");
insert into flight values("UK302", "LHR", "KHI", "05:00", "17:00", 155000 ,"ANJ-411");
insert into flight values("UK303", "LHR", "KHI", "06:00", "13:00", 115000 ,"ANJ-413");
insert into flight values("UK304", "ISL", "MUL", "07:00", "21:00", 135000 ,"ANJ-414");
insert into flight values("UK305", "KHI", "LHR", "08:00", "16:00", 135000 ,"ANJ-415");
insert into flight values("UK306", "MUL", "KHI", "09:00", "18:00", 135000, "ANJ-412");
insert into flight values("UK307", "RWL", "LHR", "02:00", "12:00", 955000 ,"ANJ-415");
insert into flight values("UK308", "LHR", "KHI", "10:00", "19:00", 215000 ,"ANJ-416");
insert into flight values("UK309", "ISL", "MUL", "08:00", "12:00", 435000 ,"ANJ-413");
insert into flight values("UK310", "KHI", "LHR", "11:00", "20:00", 335000 ,"ANJ-414");

insert into passenger values("696901", "areeb1","qamar", "lums","0332472", "pak1");
insert into passenger values("696902", "areeb1","qamar", "lums","0332472", "pak1");
insert into passenger values("696903", "areeb2","qamar", "jt", "03324","pak2");
insert into passenger values("696904", "areeb3","qamar", "mt","03324","pak3");
insert into passenger values("696905", "areeb4","qamar", "lums","0332472", "pak1");
insert into passenger values("696906", "areeb5","qamar", "jt", "03324","pak2");
insert into passenger values("696907", "areeb6","qamar", "mt","03324","pak3");
insert into passenger values("696908", "areeb7","qamar", "lums","0332472", "pak1");
insert into passenger values("696909", "areeb8","qamar", "jt", "03324","pak2");
insert into passenger values("696910", "areeb9","qamar", "mt","03324","pak3");



insert into ticket(passenger_id ,flight_id) values("696901","UK301");	
insert into ticket(passenger_id ,flight_id) values("696902","UK302");
insert into ticket(passenger_id ,flight_id) values("696903","UK303");
insert into ticket(passenger_id ,flight_id) values("696904","UK304");
insert into ticket(passenger_id ,flight_id) values("696905","UK305");
insert into ticket(passenger_id ,flight_id) values("696906","UK306");
insert into ticket(passenger_id ,flight_id) values("696907","UK307");
insert into ticket(passenger_id ,flight_id) values("696908","UK308");
insert into ticket(passenger_id ,flight_id) values("696909","UK309");
insert into ticket(passenger_id ,flight_id) values("696910","UK310");


insert into flightHistory(passenger_id ,flight_id) values("696901","UK301");	
insert into flightHistory(passenger_id ,flight_id) values("696902","UK302");
insert into flightHistory(passenger_id ,flight_id) values("696903","UK303");
insert into flightHistory(passenger_id ,flight_id) values("696904","UK304");
insert into flightHistory(passenger_id ,flight_id) values("696905","UK305");
insert into flightHistory(passenger_id ,flight_id) values("696906","UK306");
insert into flightHistory(passenger_id ,flight_id) values("696907","UK307");
insert into flightHistory(passenger_id ,flight_id) values("696908","UK308");
insert into flightHistory(passenger_id ,flight_id) values("696909","UK309");
insert into flightHistory(passenger_id ,flight_id) values("696910","UK3010");