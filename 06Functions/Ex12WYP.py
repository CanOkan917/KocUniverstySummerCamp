"""

@author: CanOkan

Functions Course (Write Your Program)

"""

def calculate_total_fee(num_of_drivers):
    total_traffic_fee = 0
    for driver in range(1, num_of_drivers + 1):
        print("Driver",driver)
        total_traffic_fee += calculate_fee()
    return total_traffic_fee

def calculate_fee():
    fee = 0
    ask = int(input('Can you blow on the breathalyzer please ? (1 for Yes, 2 for No) '))
    if ask == 2:
        fee = 3836
    elif ask == 1:
        beers = int(input("How many beers did you drink?: "))
        if beers > 2:
            fee = 1228
        else:
            print("You are free to leave.")
    else:
        fee = 1228
    return fee

#please do not change the main function
def main():
    num_of_drivers = int(input('How many drivers were caught in traffic control?: '))
    total_penalty = calculate_total_fee(num_of_drivers)
    print('Total traffic penalty:',total_penalty)

main()