from creature_list import CreatureList
from data_generator import DataGenerator
import creature_types as ctypes

def main():
  # get data
  dg = DataGenerator()
  x_data, y_data = dg.get_data()

  # Load some creatures and run a simulation
  cl = CreatureList(100, ctypes.NormalArctanCreature, x_data, y_data)
  cl.run(1)
  cl.create_chi_sq_list()
  best_cs = cl.get_n_best_creatures(5)
  for i in best_cs:
    print(i.get_chi_sq())
  #cl.run(200)



if __name__ == "__main__":
  main()