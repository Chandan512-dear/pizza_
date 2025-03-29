size=input("what size pizza you want (s/m/l)?")
bill=0
if size =='S' or size =='s':
    bill+=100
    print("small pizza price is 100 Rs.")
elif size =='M' or size =='m':
     bill+=200
     print("medium pizza price is 200 Rs.")
else:
     bill+=300
     print("Large pizza price is 300 Rs.")
add_pepperoni=input("Do you want to pepperoni(Y/N)?")
if add_pepperoni =='Y' or add_pepperoni =='y':
     if size =='S' or size =='s':
          bill+=30
    
     else:
        bill +=50

extera_cheese=input("Do you want to extra cheese(Y/N)?")
if extera_cheese=='Y' or extera_cheese == 'y':
     bill+=20
print(f"your final bill is {bill}")    
print("Thank you for using our... product!")    
