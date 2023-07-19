# Nur Selin Gökde
def init_game():
    return groups, players_in_group

# Cem Deniz
def select_shapes():
    return shapes, shape_sizes

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
    pass

main()