"""

@author: CanOkan, Fatih

Conditional Statements Course (Write Your Program)

"""

import math

package_type = int(input("What is the type of package (1=Envelope/2=Box)? "))
package_types = [ "Envelope", "Box" ]
weight_types = [ "Grams", "Kilograms" ]

envelopped_values = [ (0, 20, 3), (20, 50, 4), (50, 100, 7) ]
boxed_values = [ (0, 1, 12) ]
distance_values = [ (0, 80, 1), (80, 500, 1.5), (500, 2000, 2), (2000, 5000, 3) ]

if package_type != 1 and package_type != 2:
    print("This is not a valid package type!")
else:
    distance = int(input("What is the distance to reciver in kilometers? "))
    weight = float(input("What is the weight of the " + package_types[package_type-1].lower() + " in "+weight_types[package_type-1].lower()+"? "))
    standard_price = 0
    final_price = 0
    if package_type == 1:
        if weight >= 2000:
            print("Maximum weight limit is exceeded!")
        else:
            for i in envelopped_values:
                if i[0] < weight <= i[1]:
                    standard_price = standard_price + i[2]
                elif 100 < weight <= 2000:
                    standard_price = standard_price + 7 + (math.ceil((weight - 100) / 100) * 2)
                    break
    else:
        if weight >= 50000:
            print("Maximum weight limit is exceeded!")
        else:
            for i in boxed_values:
                if i[0] < weight <= i[1]:
                    standard_price = standard_price + i[2]
                elif 1 < weight <= 50:
                    price_to_add = 12
                    new_weight = weight - 1
                    if new_weight > 20:
                        price_to_add = price_to_add + 70
                    price_to_add = price_to_add + (math.ceil(new_weight) * 5)
                    standard_price = standard_price + price_to_add
                    break
    
    for i in distance_values:
        if i[0] < distance <= i[1]:
            final_price = final_price + (i[2] * standard_price)
        elif distance > 5000:
            final_price = final_price + (5 * standard_price)
            break

    if final_price > 0:
        print("The price is",final_price,"TL")