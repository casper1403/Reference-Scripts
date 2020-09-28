""" PDF (probability density function )"""

def pdf(mu,sigma,x):
   return (1/2(2*np.pi)**0.5) * np.exp(0.5*(x-mu)**2 / sigma**2)
