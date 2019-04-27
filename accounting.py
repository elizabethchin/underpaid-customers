melon_cost = 1.00

customer_name = "Joe"
customer_melons = 5
customer_paid = 5.00

file = customer-orders.txt

def accounting(file):
    """Calculates discrepncies in customer bill"""

    the_file = open(file)
    for line in file:
        line = line.rstrip()
        words = line.split("|")

        customer_name, customer_melons, customer_paid = words
     
    customer_expected = words[0] * melon_cost
    if customer_expected != words[2]:
        print(f"{words[0]} paid ${words[2]:.2f},",
            f"expected ${customer_expected:.2f}"
            )
    the_file.close()
