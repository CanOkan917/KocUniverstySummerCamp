SHAPES = {1:"Square", 2:"Triangle", 3:"Equilateral triangle", 4:"Sandglass"}

# Nur Selin Gökde
def init_game():
    
    
    return groups, players_in_group

# Cem Deniz
def select_shapes():
    return error, shapes, shape_sizes

# Can Okan
def generate_shape(shape_id, size):
    return shape, total_stars

# Fatih Yılmaz
def main():
    #calling group and player values from init_game()
    groups, players = init_game()
    
    # * Group i - Player j *
    for i in range(1, groups + 1):
        
        for j in range(1, players + 1):
            
            alive_players = 0
            
            print(f"*Group {i} - Player {j} *")
            
            #calling shape number and size of the shape from select_shapes()
            error, shape_number, size = select_shapes()
            
            if error == True: #if shape number isn't valid:
                print(f"Oops invalid choice! Player {j} is eliminated!")
            
            else: #if user inputs an invalid shape number, like 7
                
                print("Shape is", SHAPES[shape_number], "!")
                
                #calling shape and amount of stars from generate_shape()
                shape, total_stars = generate_shape(shape_number, size)
                
                #asking for star amount
                stars = int(input("How many stars exist in this " + SHAPES[shape_number] + "?"))
                print(shape)
                
                #checks if player guesses the amount of stars correct or not
                if stars != total_stars: 
                    print(f"Total number of stars: {total_stars}. Oops, Player {j} is eliminated!")
                else:
                    print(f"Total number of stars: {total_stars}. Player {j} wins the game!")
                    alive_players += 1
        print(f"{alive_players} player(s) stayed alive in Group {i} !")       
    

    print("\n----End of the game----")

main()

#VsCode theme
#flate punk italic