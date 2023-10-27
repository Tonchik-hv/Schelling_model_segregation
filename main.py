import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import os
import ctypes


mylib = ctypes.CDLL('./mylib.so')
# Define the argument types and return type of the function
mylib.count_neighbours.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
mylib.count_neighbours.restype = ctypes.c_int

# def count_neighbours(MAP, row_num, col_num, val):
#     sl0 = np.array(range(row_num-1,row_num+2)).reshape(-1,1)%MAP.shape[0]
#     sl1 = np.array(range(col_num-1,col_num+2)).reshape(1,-1)%MAP.shape[1]
#     neighbourhood = MAP[sl0, sl1]
#     n_neighbours = len(np.where(neighbourhood == val)[0])-1
#     return n_neighbours


def python_list_to_c_array(data):
    # Create an array of arrays (rows)
    c_rows = (ctypes.POINTER(ctypes.c_int) * len(data))()
    for i, row in enumerate(data):
        # Convert each row to an array
        c_rows[i] = (ctypes.c_int * len(row))(*row)
    # Create a pointer to the array of arrays
    c_data = ctypes.cast(c_rows, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)))

    return c_data


class Schelling_model:
  def __init__(self, size=100, threshold=0.5, max_iter=50):
    self.size = size
    self.threshold = threshold
    self.max_iter = max_iter
    self.init_map = np.random.randint(low=0, high=2, size=(size, size))
    self.map = copy.deepcopy(self.init_map)
    self.map_history = [copy.deepcopy(self.init_map)]
    self.num_dissap_evol = []

  def plot_init_map(self, filename='initial_map.png'):
    plt.imshow(self.init_map, cmap='binary')
    plt.savefig(filename)

  def one_iter(self):
    market = {}
    dissapointed = []
    number = 0

    c_array = python_list_to_c_array(self.map)

    for (row, col), val in np.ndenumerate(self.map):
      #n_neighbours = count_neighbours(self.map, row, col, val)
      n_neighbours = mylib.count_neighbours(c_array, self.map.shape[0], self.map.shape[1], row, col, val)
      if n_neighbours < self.threshold*8:
          market[(row, col)] = number
          dissapointed.append(val)
          number += 1
    if len(dissapointed) != 0:
      random.shuffle(dissapointed)
      for key in market:
        self.map[key[0], key[1]] = dissapointed[market[key]]
      self.map_history.append(copy.deepcopy(self.map))
    self.num_dissap_evol.append(len(dissapointed))

  def play_game(self):
    for _ in range(self.max_iter):
      self.one_iter()

  def plot_final_map(self, filename='result.png'):
    plt.imshow(self.map_history[-1], cmap='binary')
    plt.savefig(filename)


if __name__ == '__main__':

    plt.rcParams["figure.figsize"] = [7, 7]

    R = 1/2
    MAX_ITER = 50

    schel_model = Schelling_model(threshold=R, max_iter=MAX_ITER)
    schel_model.play_game()
    schel_model.plot_init_map()
    schel_model.plot_final_map()