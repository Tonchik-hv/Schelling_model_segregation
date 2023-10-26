import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import os


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

  def count_neighbours(self, row_num, col_num, val):
    sl0 = np.array(range(row_num-1,row_num+2)).reshape(-1,1)%self.map.shape[0]
    sl1 = np.array(range(col_num-1,col_num+2)).reshape(1,-1)%self.map.shape[1]
    neighbourhood = self.map[sl0, sl1]
    n_neighbours = len(np.where(neighbourhood == val)[0])-1
    return n_neighbours

  def one_iter(self):
    market = {}
    dissapointed = []
    number = 0
    for (row, col), val in np.ndenumerate(self.map):
      n_neighbours = self.count_neighbours(row, col, val)
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

  def plot_final_map(self, , filename='result.png'):
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
