# Solves sodoku puzzles and outputs first solution
# Outputs time to get to solution
import time

def solve(puzzle):
    start_time = time.time()
    locked_items = []
    temp_row = []

    # go through puzzle and assign 0 to unset values a 1 to set values also put input values into new array
    for row in puzzle:
        for item in row:
            if item == 0:
                temp_row.append(0)
            else:
                temp_row.append(1)
        locked_items.append(temp_row.copy())
        temp_row.clear()
    moving_forward = True
    index_box = [0, 0]

    # go until either we go off the beginning which means there are no 
    # solutions or the end which means we found a solution
    while -1 < index_box[0] < 9:
        if locked_items[index_box[0]][index_box[1]] != 1:
            counter = puzzle[index_box[0]][index_box[1]]
            # try to put every value in the current cell
            while 0 < 1:
                if put(puzzle, int(counter + 1), index_box[0], index_box[1]):
                    puzzle[index_box[0]][index_box[1]] = counter + 1
                    moving_forward = True
                    break
                else:
                    # if we reach here then no value is possible for puzzle[index_box[0]][index_box[1]] so set it to 0 and move backwards
                    if counter >= 8:
                        puzzle[index_box[0]][index_box[1]] = 0
                        moving_forward = False
                        break
                    counter += 1
        # move forward or backwards depending on our direction
        if moving_forward:
            index_box = next_box(index_box)
        else:
            index_box = last_box(index_box)
    # output puzzle and details
    print("Time Elapsed: " + str(round(time.time() - start_time, 2)) + " seconds")
    if index_box[0] >= 9:
        print("Solved")
        for line in puzzle:
            print(line)
    else:
        print("The Puzzle is Impossible")

# get the next box by checking to see if we should go to the next row
def next_box(current_box):
    if current_box[1] != 8:
        return [current_box[0], current_box[1] + 1]
    else:
        return [current_box[0] + 1, 0]


# get the last box by checking if we should wrap up to last line
def last_box(current_box):
    if current_box[1] != 0:
        return [current_box[0], current_box[1] - 1]
    else:
        return [current_box[0] - 1, 8]


# try to put a value in a give row and column
def put(puzzle, input_value, row, column):
    # make sure input is valud
    if input_value > 9:
        return False
    # make sure the value doesnt appear in the same row and column
    for value in range(0, 9):
        if puzzle[row][value] == input_value and not column == value:
            return False
        if puzzle[value][column] == input_value and not row == value:
            return False
    # check the values in the same block to make sure input_value dosent appear there
    for v1 in range(int(row / 3) * 3, int(row / 3) * 3 + 3):
        for v2 in range(int(column / 3) * 3, int(column / 3) * 3 + 3):
            if input_value == puzzle[v1][v2] and (row != v1 and column != v2):
                return False
    return True


puzzle1 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 3, 6, 0, 0, 0, 0, 0],
           [0, 7, 0, 0, 9, 0, 2, 0, 0],
           [0, 5, 0, 0, 0, 7, 0, 0, 0],
           [0, 0, 0, 0, 4, 5, 7, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 3, 0],
           [0, 0, 1, 0, 0, 0, 0, 6, 8],
           [0, 0, 8, 5, 0, 0, 0, 1, 0],
           [0, 9, 0, 0, 0, 0, 4, 0, 0]]

solve(puzzle1)
