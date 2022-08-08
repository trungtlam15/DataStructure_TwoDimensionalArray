def print_two_dimensional_array(twod_array):
  for row in twod_array:
    for column in row:
      print(column, '\t', end='')
    print()
    print('5')


def check_two_dimensional_array(twod_array):
  row_max = 0
  row_max = 0
  column_max = 0
  max_value = twod_array[row_max][column_max]
  for i in range(len(twod_array)):
    for j in range(len(twod_array[i])):
      if twod_array[i][j] > max_value:
        row_max = i
        column_max = j
        max_value = twod_array[i][j]
  print("max row ", row_max, "max colum ", column_max, "max value ", max_value)
  print("max row ", row_max, "max colum ", column_max, "max value ", max_value)
  print("max row ", row_max, "max colum ", column_max, "max value ", max_value)


def print_above_primary_diagonal(twod_array):
  for i in range(len(twod_array)):
    for j in range(len(twod_array[i])):
      if j > i:
        print(twod_array[i][j])


def print_on_and_below_primary_diagonal(twod_array):
  for i in range(len(twod_array)):
    for j in range(len(twod_array[i])):
      if j <= i:
        print(twod_array[i][j])


def print_above_secondary_diagonal(twod_array):
  for i in range(len(twod_array)):
    for j in range(len(twod_array[i])):
      if i + j < len(twod_array) - 1:
        print(twod_array[i][j])


def print_on_and_below_secondary_diagonal(twod_array):
  for i in range(len(twod_array)):
    for j in range(len(twod_array[i])):
      if i + j >= len(twod_array) - 1:
        print(twod_array[i][j])


def sum_row(twod_array):
  sum_row = 0
  choosing_row = int(input("enter row index"))
  for i in range(len(twod_array)):
    sum_row = sum_row + twod_array[choosing_row][i]
  print(sum_row)


def sum_column(twod_array):
  sum_column = 0
  choosing_column = int(input("enter column index: "))
  for i in range(len(twod_array)):
    sum_column = sum_column + twod_array[i][choosing_column]
  print(sum_column)


def find_max_in_row(twod_array):
  choosing_row = int(input("enter row index: "))
  for i in range(len(twod_array)):
    max_row = twod_array[choosing_row][i]
    if twod_array[choosing_row][i] > max_row:
      max_row = twod_array[choosing_row][i]
  print(max_row)


if __name__ == '__main__':
  T = [[11, 12, 5, 2], [15, 6, 10, 7], [10, 8, 12, 5], [12, 15, 8, 6]]

  print_two_dimensional_array(T)

  # check_two_dimensional_array(T)

  # print_above_primary_diagonal(T)

  # print_on_and_below_primary_diagonal(T)

  # print_above_secondary_diagonal(T)

  # print_on_and_below_secondary_diagonal(T)

  # sum_row(T)

  # sum_column(T)

  # find_max_in_row(T)
