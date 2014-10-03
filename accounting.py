def identify_underpaying_customers(filename):
    """From file, identify which customers underpaid and print amount data"""

    # open file
    file = open(filename)

    # read file and break lines into customer data
    for line in file:
        # separate customer data into name, melons bought and amount paid
        customer_data = line.split(",")
        customer_name = customer_data[1]
        melons_bought = int(customer_data[2])
        amount_paid = float(customer_data[3])

        # check if customer underpaid
        amount_owed = melons_bought * MELON_COST
        if  amount_paid < amount_owed:
            # determine and print amount customer still owes
            amount_past_due = amount_owed - amount_paid
            print "%s: paid $%.2f, expected $%.2f, owes $%.2f" % (customer_name, amount_paid, amount_owed, amount_past_due)


MELON_COST = 1.00

def main():
    
    identify_underpaying_customers("customer_orders.csv")

if __name__ == "__main__":
    main()
