
total_amount = float(input("Enter the total amount of the purchase: "))

num_items = int(input("Enter the number of items: "))

day_of_week = input("Enter the day of the week: ").strip().capitalize()

discount = 0

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount += 10  
elif day_of_week in ["Saturday", "Sunday"]:
    discount += 20 
else:
    print("Invalid day of the week. No discount will be applied.")

if num_items > 5:
    discount += 5  

final_price = total_amount * (1 - discount / 100)

print(f"The total price after discounts is: ${final_price:.2f}")
