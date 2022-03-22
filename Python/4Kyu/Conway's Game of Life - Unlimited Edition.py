import imp
import numpy as np
test = imp.load_source('test', './test.py')

def trim_board(cells):
    while True:
        if sum(cells[0]) > 0:
            break
        else:
            cells = np.delete(cells,0,0)

    while True:
        if sum(cells[-1]) > 0:
            break
        else:
            cells = np.delete(cells,-1,0)

    while True:
        if sum(cells[0 : len(cells), 0]) > 0:
            break
        else:
            cells = np.delete(cells,0,1)

    while True:
        if sum(cells[0 : len(cells), -1]) > 0:
            break
        else:
            cells = np.delete(cells,-1,1)

    return cells




def iterate_generation(cells):
    new_cells = cells.copy()
    for i in range(1, len(cells)-1):
        for j in range(1, len(cells[i])-1):
            new_cells[i,j] = 1
            neighbours = cells[i-1:i+2, j-1:j+2]
            neighbour_sum = np.sum(neighbours) - cells[i,j]
            if neighbour_sum == 2: 
                new_cells[i,j] = cells[i,j]
            elif neighbour_sum == 3: 
                new_cells[i,j] = 1
            else:
                new_cells[i,j] = 0
    return new_cells


def get_generation(cells, generations):
    cells = np.pad(cells, generations+1, 'constant', constant_values=(0))
    for gen in range(generations):
        cells = iterate_generation(cells)
       
    cells = trim_board(cells)
    return [c.tolist() for c in cells]

start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]

resp = get_generation(start, 1)
test.assert_equals(resp, end)
