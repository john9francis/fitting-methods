from creature import Creature
import numpy as np
from matplotlib import pyplot as plt

def main():
  # get data
  data = [.1,1.,2.,3.,2.,5.,2.,2.,2.,1.,.1]

  # get a creature and test the fit
  c = Creature()
  c.set_data(data)
  c.plot_fit()


if __name__ == "__main__":
  main()