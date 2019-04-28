melon_cost = 1.00

def accounting(file):
    """Calculates discrepncies in customer bill"""

    the_file = open(file) #opens file
    for line in the_file:
        line = line.rstrip()
        words = line.split("|")

        customer_name = words[1]
        melons_purchased = float(words[2])
        amt_paid = float(words[3])


    the_file.close()

    customer_expected = melons_purchased * melon_cost
    if customer_expected != amt_paid:
        print(f"{customer_name} paid ${amt_paid:.2f}, expected", 
        f"${customer_expected:.2f}")
    

print(accounting("customer-orders.txt"))

