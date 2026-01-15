# Python program for A* Search Algorithm
import heapq


# Define the Cell class
class Cell:
    def __init__(self):
        # Parent cell's row index
        self.parent_y = 0
        # Parent cell's column index
        self.parent_x = 0
        # Total cost of the cell (g + h)
        self.f = float("inf")
        # Cost from start to this cell
        self.g = float("inf")
        # Heuristic cost from this cell to destination
        self.h = 0


# Define the size of the grid
ROW = 9
COL = 10


# FIX: Check if a cell is valid (within the grid limits)
def is_valid(row, col):
    """Check if a cell is within the grid"""
    pass


# FIX: Check if a cell is unblocked
def is_unblocked(grid, row, col):
    """Whether the cell is a valid cell with number 1  or not."""
    pass


# FIX: Check if a cell is the destination
def is_destination(row, col, dest):
    """Are we on the destination cell or not?"""
    pass


# FIX: Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    """Our heuristic function for estimation."""
    pass


# Trace the path from source to destination
def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (
        cell_details[row][col].parent_y == row
        and cell_details[row][col].parent_x == col
    ):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_y
        temp_col = cell_details[row][col].parent_x
        row = temp_row
        col = temp_col

    # Add the source cell to the path
    path.append((row, col))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()


# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(
        grid, dest[0], dest[1]
    ):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    y = src[0]
    x = src[1]
    cell_details[y][x].f = 0
    cell_details[y][x].g = 0
    cell_details[y][x].h = 0
    cell_details[y][x].parent_y = y
    cell_details[y][x].parent_x = x

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, y, x))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        y = p[1]
        x = p[2]
        closed_list[y][x] = True

        # For each direction, check the successors
        directions = [
            (0, 1),  # RIGHT
            (0, -1),  # LEFT
            (1, 0),  # UP
            (-1, 0),  # DOWN
        ]

        for dir in directions:
            new_y = y + dir[0]
            new_x = x + dir[1]

            # If the successor is valid, unblocked, and not visited
            if (
                is_valid(new_y, new_x)
                and is_unblocked(grid, new_y, new_x)
                and not closed_list[new_y][new_x]
            ):
                # If the successor is the destination
                if is_destination(new_y, new_x, dest):
                    # Set the parent of the destination cell
                    cell_details[new_y][new_x].parent_y = y
                    cell_details[new_y][new_x].parent_x = x
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # FIX: Calculate the new f, g, and h values
                    pass

                    # If the cell is not in the open list or the new f value is smaller
                    # Add the cell to the open list
                    # Update the cell details

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")


# Driver Code
def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    ]

    # Define the source and destination
    src = [8, 0]
    dest = [0, 0]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()
