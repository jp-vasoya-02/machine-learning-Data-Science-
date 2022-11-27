import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(nrows=2,ncols=1)
for ax in axes:
    ax.plot(np.arange(20),np.random.randint(1,50,20),"g")
    ax.set_xlabel("X axis")
plt.tight_layout()
plt.show()