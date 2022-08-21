
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y1 = x**2
y2 = 2*x + 3
print(x)
print(y1)
print(y2)
plt.plot(x,y1,color='red',label="Apple",marker='o')

plt.plot(x,y2,color='green',label="kiwi",linestyle='dashed')
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Prices of fruit over time")
plt.legend()
plt.show()