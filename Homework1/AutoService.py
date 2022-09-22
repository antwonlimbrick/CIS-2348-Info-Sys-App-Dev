
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
 
oilChange = 35;
 
tireRotation = 19;
 
carWash = 7;
 
carWax = 12;
 
tot = 0;
 
serv1 = 0;
 
serv2 = 0;
 
first_serv = input("Select first service:\n")

 
if (first_serv == "Oil change"):
    tot = tot + oilChange;
    serv1 = oilChange;
    
elif (first_serv == "Tire rotation"):
    tot = tot + tireRotation;
    serv1 = tireRotation;
    
elif (first_serv == "Car wash"):
    tot = tot + carWash;
    serv1 = carWash;
    
elif (first_serv == "Car wax"):
    tot = tot + carWax;
    serv1 = carWax;
    
elif (first_serv == "-"):
    first_serv = "No service";
    tot = tot + 0;
 


second_serv = input("Select second service:\n")
 
if (second_serv == "Oil change"):
    tot = tot + oilChange;
    serv2 = oilChange;
    
elif (second_serv == "Tire rotation"):
    tot = tot + tireRotation;
    serv2 = tireRotation;
    
elif (second_serv == "Car wash"):
    tot = tot + carWash;
    serv2 = carWash;
    
elif (second_serv == "Car wax"):
    tot = tot + carWax;
    serv2 = carWax;
    
elif (second_serv == "-"):
    second_serv = "No service";
    serv2 = 0;
    tot = tot + 0;
    
print()
 
 
print("Davy's auto shop invoice")
 
print()
 
if (first_serv == "No service") and (second_serv == "No service"):
    print("Service 1: " + first_serv)
    print("Service 2: " + second_serv)
    print()

elif (second_serv == "No service"):
    print("Service 1: " + first_serv + ", $" + str(serv1))
    print("Service 2: " + second_serv)
    print()
 
elif (first_serv == "No service"):
    print("Service 1: " + first_serv)
    print("Service 2: " + second_serv + ", $" + str(serv2))
    print()
 
else:
    print("Service 1: " + first_serv + ", $" + str(serv1))
    print("Service 2: " + second_serv + ", $" + str(serv2))
    print()
 
print("Total: $" + str(tot))
