

def print_two_dimensional_array(twod_array):
    for row in twod_array:
        for column in row:
            print(column)

if __name__ == '__main__':
    T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
    print_two_dimensional_array(T)


