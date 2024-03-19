from creature_list import CreatureList
from data_generator import DataGenerator
import numpy as np
from matplotlib import pyplot as plt

def main():
  # get data
  dg = DataGenerator()
  x_data, y_data = dg.get_data()

  # get a creature and test the fit

  initial_guess = [1700, 2, 60, -185, 240, 255, 145]

  cl = CreatureList(100, x_data, y_data, initial_guess)
  cl.run(500)


if __name__ == "__main__":
  main()