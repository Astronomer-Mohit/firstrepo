#pi = 3.14159
def MySineWave(x):
    import numpy as np
    import matplotlib.pyplot as plt
	t = np.arange(-np.pi*2, np.pi*2, 0.1)
	plt.plot(t, np.cos(2*np.pi*(t/x)))
    plt.show()
