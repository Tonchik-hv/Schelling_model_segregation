from source import *
import sys

def main(size=100, threshold=1/2):
  argv_list = sys.argv
  if len(argv_list) == 2:
    size = int(argv_list[1])
  elif len(argv_list) == 3:
    size = int(argv_list[1])
    threshold = float(argv_list[2])

  plt.rcParams["figure.figsize"] = [7, 7]

  print(f"Running with params:\nsize={size}\nthreshold={threshold}")
  schel_model = Schelling_model(size=size, threshold=threshold)
  schel_model.play_game()
  # print(schel_model.map)
  schel_model.plot_init_map()
  schel_model.plot_final_map()


if __name__ == '__main__':
  main()
    