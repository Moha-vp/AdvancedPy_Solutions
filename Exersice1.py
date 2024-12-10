name =input("Enter your name")

if name=="VIP":

 print("enjoy the show for free")

else:
    
 try:
        tickets=int(input("how many tickets do want to buy ?"))
        ticket_price=15.50
        total_cost=tickets*ticket_price
        
        print(f"the total cost for {tickets} is:${total_cost:.2f}")
        
 except ValueError :
        print("please enter a valid number of tickets.")