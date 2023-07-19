SHAPES = {1:"Square", 2:"Triangle", 3:"Equilateral triangle", 4:"Sandglass"}

# Nur Selin Gökde
def init_game():
    groups = int(input("How many groups are there: "))
    players_in_group = int(input("\nHow many players are there in the group: "))
    return groups, players_in_group

# Cem Deniz
def select_shapes():
    shape = int(input("\nSelect a shape (1 Square, 2 Triangle, 3 Equilateral triangle, 4 Sandglass): "))
    if shape in SHAPES:
        print(f'\nShape is { SHAPES[shape] }!')
        if shape == 4:
            size = int(input("\nSelect the size of shape (Size must be odd!): "))
            if size > 0 and size % 2 == 1:
                return False, shape, size
        else:
            size = int(input("\nSelect the size of shape (2/3/4/5/6): "))
            if size>=2 and size<=6:
                return False, shape, size
    return True, 0, 0

# Can Okan
def generate_shape(shape_id, size):
    shape = ""
    total_stars = 0
    if shape_id == 1:
        for row in range(size):
            if row != 0:
                shape += "\n"
            for col in range(size):
                shape += "* "
                total_stars += 1
    elif shape_id == 2:
        for row in range(1, size + 1):
            if row != 1:
                shape += "\n"
            for _ in range(size - row):
                shape += "  "
            for _ in range(row):
                shape += "* "
                total_stars += 1
    elif shape_id == 3:
        for row in range(size):
            if row != 0:
                shape += "\n"
            for _ in range(row):
                shape += " "
            for _ in range(size - row):
                shape += "* "
                total_stars += 1
    elif shape_id == 4:
        n_rows = 0
        c = 1
        while c <= size:
            c += 2
            n_rows += 1
        for row in range(n_rows, 0, -1):
            for _ in range(n_rows - row):
                shape += " "
            for _ in range(1, 2 * row):
                shape += "*"
                total_stars += 1
            shape += "\n"
        for row in range(2, n_rows + 1):
            for _ in range(n_rows - row):
                shape += " "
            for _ in range(1, 2 * row):
                shape += "*"
                total_stars += 1
            if row != n_rows:
                shape += "\n"
    return shape, total_stars

# Fatih Yılmaz
def main():
    #calling group and player values from init_game()
    groups, players = init_game()
    
    # * Group i - Player j *
    for i in range(1, groups + 1):
        alive_players = 0
        
        for j in range(1, players + 1):
            
            print(f"\n* Group {i} - Player {j} *")
            
            #calling shape number and size of the shape from select_shapes()
            error, shape_number, size = select_shapes()
            
            if error == True: #if shape number isn't valid:
                print(f"\nOops invalid choice! Player {j} is eliminated!")
            
            else: #if user inputs an invalid shape number, like 7
                
                #calling shape and amount of stars from generate_shape()
                shape, total_stars = generate_shape(shape_number, size)
                
                #asking for star amount
                stars = int(input("\nHow many stars exist in this " + SHAPES[shape_number] + "? "))
                print()
                print(shape)
                
                #checks if player guesses the amount of stars correct or not
                if stars != total_stars: 
                    print(f"\nTotal number of stars: {total_stars}. Oops, Player {j} is eliminated!")
                else:
                    print(f"\nTotal number of stars: {total_stars}. Player {j} wins the game!")
                    alive_players += 1
        print(f"\n{alive_players} player(s) stayed alive in Group {i} !\n")       
    

    print("\n----End of the game----")

main()