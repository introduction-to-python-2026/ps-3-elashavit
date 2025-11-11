def approximate_pi(n_terms):
  leibniz_series = []
  for i in range(n_terms):
      thing = (-1)**i/(2*i+1)
      leibniz_series.append(thing)
  return (sum(leibniz_series)*4)
