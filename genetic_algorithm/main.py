from creature_list import CreatureList
from data_generator import DataGenerator

def main():
  # get data
  dg = DataGenerator()
  x_data, y_data = dg.get_data()

  # get a creature and test the fit
  cl = CreatureList(100, x_data, y_data)
  cl.run(300)


if __name__ == "__main__":
  main()