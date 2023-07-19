SHAPES = {1:"Square", 2:"Triangle", 3:"Equilateral triangle", 4:"Sandglass"}

# Nur Selin Gökde
def init_game():
    return groups, players_in_group

# Cem Deniz
def select_shapes():
    shape=int(input("Enter a shape(1 Square, 2 Triangle, 3 Equilateral triangle, 4 Sandglass): "))
    if shape in SHAPES:
        print(f'Shape is { SHAPES[shape] }!')
        if shape==4:
            size=int(input("Select the size of shape (Size must be odd!): "))
            if size>0 and size%2==1:
                return False, shape, size
        else:
            size=int(input("Select the size of shape (2/3/4/5/6): "))
            if size>=2 and size<=6:
                return False, shape, size
    return True, 0, 0

# Can Okan
def generate_shape(shape_id, size):
    return shape, total_stars

# Fatih Yılmaz
def main():
    pass

main()