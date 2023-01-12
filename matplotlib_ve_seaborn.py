import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100) # 0 ile 10 arasında 100 sayı oluştur
y = np.linspace(-5,5,100)

#print(x,y)

fig = plt.figure()
ax = fig.add_subplot(111) #ax eksen in ksaltması
#111 deki satı sayısı sütün sayısı ve kaç resim geleceğidir.
ax.plot(x,y, color = "red",linewidth =3)
ax.scatter(x,y, color = "green", marker ="*")


plt.xlabel("x")
plt.ylabel("y")
plt.title("x vs y")
plt.savefig("x_y.png")
plt.show()

# seaborn

import seaborn as sns

a = np.random.randint(5, size = 1000)

plt.figure()
sns.countplot(a)


