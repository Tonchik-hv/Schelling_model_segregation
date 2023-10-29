from source import *

def main(threshold=1/2, max_iter=50):
  plt.rcParams["figure.figsize"] = [7, 7]

  schel_model = Schelling_model(threshold=threshold, max_iter=max_iter)
  schel_model.play_game()
  # print(schel_model.map)
  schel_model.plot_init_map()
  schel_model.plot_final_map()


if __name__ == '__main__':
  main()
    