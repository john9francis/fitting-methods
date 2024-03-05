from grid_search import GridSearch

def main():
  grid_search = GridSearch()
  chi_2 = grid_search.calc_chi_squared()
  #grid_search.plot_data_and_fit()
  #grid_search.plot_chisq_for_varying_a1()
  grid_search.plot_chisq_for_varying_mu1()


if __name__ == "__main__":
  main()