people=int(input("Enter the number of people needing a ride:"))

taxi_cap=int (input("Enter the number of people that can fit in one taxi "))
taxi_req=people // taxi_cap
if people % taxi_cap != 0:
    taxi_req +=1 
    
print(f"The number of taxis required is: {taxi_req}")