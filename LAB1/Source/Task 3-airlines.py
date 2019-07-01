from AirlineReservation import Passenger, Employee, Ticket, Flight

# p_id,p_type,p_gender,p_name,p_phonenumber,f_id,pno,f_origin,f_destination,no_of_stops,flight_type
#f_id, f_origin, f_destination, no_of_stops, flight_type, p_id, p_type
f1 = Flight("AA1568", "PHX", "MCI", 1, "AMERICAN EAGLE", "P1", "P4")
f1.get_flight_details("AE1425")

#Instances of Passenger class
p1 = Passenger("P1", "P", "F", "Naveena", 4257896358, "F1855", "A103", "MCI", "HYD", 3, "American Airlines")
p2 = Passenger("P2", "P", "F", "Thoshitha", 2589796358, "F1725", "A183", "MCI", "HYD", 3, "British Airways")
p3 = Passenger("P3", "P", "F", "Sravanthi", 42597961558, "F1520", "A173", "MCI", "BLR", 3, "QATAR")

#Instances of Employee class
e1 = Employee("E1", "E", "M", "Hitesh", 4257896358, "F1855", "A103", "MCI", "HYD", 3, "American Airlines")
e2 = Employee("E2", "E", "M", "Raghav", 2589796358, "F1725", "A183", "MCI", "HYD", 3, "British Airways")
e3 = Employee("E2", "E", "F", "ASHA", 42597961558, "F1520", "A173", "MCI", "BLR", 3, "QATAR")

#This method prints the travel details for the passenger
p1.get_travel_details_passanger()
#This method prints the travel details for the employee
e1.get_travel_details_employee()

#This method prints the travelling passengers on that flight
p1.get_travelling_passengers()

#Prints the boarding pass
T1 = Ticket("P1", "P", "F", "CHINNU", 42597961558, "F1520", "A173", "MCI", "BLR", 3, "QATAR", "G", "E",12)
T1.get_boarding_pass("CHINNU")





