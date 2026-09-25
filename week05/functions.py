def print_square(size: int, fill_char: str):
    for i in range(size):
        print(fill_char * size)


def draw_square(outside_size: int, 
                inside_size: int, 
                fill_char: str, 
                hollow_char: str):

    # check if sizes are ok
    if outside_size > inside_size + 1:
        hollow_lines = inside_size
        non_hollow_lines = outside_size - inside_size
        outside_border_size = non_hollow_lines // 2
        # print top half
        for line in range(outside_border_size):
            print(fill_char * outside_size)
        # print the middle part
        for line in range(hollow_lines):
            print(fill_char * outside_border_size, end = "")
            print(hollow_char * inside_size, end ="")
            print(fill_char * outside_border_size)
        # print the bottom part
        for line in range(outside_border_size):
            print(fill_char * outside_size)
        
    else:
        print("Tell something nasty to the client")

