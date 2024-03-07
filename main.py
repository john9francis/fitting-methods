from grid_search import GridSearch

def main():
  # set initial guesses:
  mu1 = 102.1
  mu2 = 177.9
  gamma1 = 30
  gamma2 = 20
  a1 = 1826
  a2 = 2812  

  mu_gamma_a_list = [mu1, mu2, gamma1, gamma2, a1, a2]

  grid_search = GridSearch(*mu_gamma_a_list)

  grid_search.minimize_chi_squared()
  print(f"Final chi squared: {grid_search.get_reduced_chi_sq()}")

  grid_search.plot_data_and_fit()


if __name__ == "__main__":
  main()