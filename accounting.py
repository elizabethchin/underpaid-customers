melon_cost = 1.00

def accounting(file):
    """Calculates discrepncies in customer bill"""

    the_file = open(file) #opens file
    for line in the_file:
        line = line.rstrip()#removes white space
        words = line.split("|")#creates list of strings

        customer_name = words[1] #gets customers name
        melons_purchased = float(words[2]) #gets melons purchased, change to float
        amt_paid = float(words[3])#gets amount paid, change to float


    the_file.close() #close file bc finished

    customer_expected = melons_purchased * melon_cost#cal what customer owes
    if customer_expected != amt_paid:#if customer didn't pay what was owed
        print(f"{customer_name} paid ${amt_paid:.2f}, expected", 
        f"${customer_expected:.2f}")
    

print(accounting("customer-orders.txt"))

