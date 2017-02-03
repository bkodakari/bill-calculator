def calculate_tip(billamount, tippercentage):
    return billamount * tippercentage


def total_bill(billamount, tiptotal):
    return billamount + tiptotal


def split_bill(total, number_people):
    return total / number_people


def main():
    what_option = int(raw_input("What would you like to do? 1 - Calculate the tip, 2 - Split the bill "))
    if what_option == 1:
        bill_amount = int(raw_input("What is the bill amount?"))
        tip_percentage = float(raw_input("What percentage do you want to tip?")) / 100
        print calculate_tip(bill_amount, tip_percentage)
        split_option = raw_input("Do you want to split the bill? Y/N : ")
        if split_option.lower() == "y":
            num_people = int(raw_input("How many people are splitting the bill?"))
            print split_bill(total_bill, num_people)
        else:
            calculate_tip(bill_amount, tip_percentage)
    else:
        num_people = int(raw_input("How many people are splitting the bill?"))
        print split_bill(total_bill, num_people)


if __name__ == '__main__':
    main()
