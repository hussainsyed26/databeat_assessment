#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_components(adjacency, rows, columns, matrix):
    """
    Count the number of connected components in the given matrix.

    Parameters:
    - adjacency (int): Type of adjacency to consider (1-4 for specific directions, 5 for all directions).
    - rows (int): Number of rows in the matrix.
    - columns (int): Number of columns in the matrix.
    - matrix (list): 2D matrix representing the grid.

    Returns:
    - int: Number of connected components in the matrix.
    """

    def is_valid(x, y):
        """Check if the given coordinates are within the matrix bounds."""
        return 0 <= x < rows and 0 <= y < columns

    def dfs(x, y, component_number):
        """
        Perform depth-first search to explore connected components in the matrix.

        Parameters:
        - x (int): Current row index.
        - y (int): Current column index.
        - component_number (int): Number assigned to the current connected component.
        """
        matrix[x][y] = component_number
        visited[x][y] = True
        for dx, dy in directions[adjacency]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and matrix[new_x][new_y] == 1 and not visited[new_x][new_y]:
                dfs(new_x, new_y, component_number)

    # Define directions for each adjacency type
    directions = {
        1: [(0, 1), (0, -1)],  # Horizontal
        2: [(1, 0), (-1, 0)],  # Vertical
        3: [(1, 1), (-1, -1), (1, -1), (-1, 1)],  # Diagonal
        4: [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Horizontal_Vertical
        5: [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # All Directions
    }

    component_count = 0
    visited = [[False] * columns for _ in range(rows)]

    # Iterate through each cell in the matrix
    for i in range(rows):
        for j in range(columns):
            # If the cell is part of a new component and not visited
            if matrix[i][j] == 1 and not visited[i][j]:
                component_count += 1
                dfs(i, j, component_count)

    return component_count


if __name__ == "__main__":
    # Get input for adjacency type
    adjacency_type = int(input("Enter the type of adjacency (1-5) (1 - horizontal; 2 - vertical; 3 - diagonal; 4 - Horizontal_Vertical; 5 - all directions): "))

    # Get input for matrix size
    rows, columns = map(int, input("Enter the number of rows and columns (separated by space): ").split())

    # Get the matrix input
    print("Enter the matrix rows (separated by spaces) individually :")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Calculate and print the total number of connected components
    total_components = count_components(adjacency_type, rows, columns, matrix)
    print("Total connected components:", total_components)
    
    # Keep the console window open until the user presses Enter
    input("Press Enter to exit...")
