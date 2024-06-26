from creature_list import CreatureList
from data_generator import DataGenerator
import creature_types as ctypes

def main():
  # get data
  dg = DataGenerator()
  x_data, y_data = dg.get_data()

  # Load some creatures and run a simulation
  cl = CreatureList(100, ctypes.Lorentz_Normal_Arctan_Creature, x_data, y_data)
  cl.run(100)



if __name__ == "__main__":
  main()