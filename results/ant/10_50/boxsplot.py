import matplotlib.pyplot as plt

brenda10 = [46.22 ,65.06 ,52.05 ,23.00 ,52.17 ,37.42 ,44.29 ,18.54 ,24.89 ,10.73]
davi10 = [96.84 , -7.82 , 50.14 , 153.10, 482.97, 78.16 , 65.86 , 191.77, 717.60, 579.02]
larissa10 = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]
super_davi10 = [1148.55 ,1232.64 ,1325.25 ,1113.42 ,1779.86 ,1049.20 ,1247.03 ,1276.91 ,1534.24 ,1227.99]
super_larissa10 = [2177.77, 2452.94, 1895.77, 2076.73, 2284.56, 2111.33, 2382.91, 2411.67, 1876.22, 2400.18]

data = [brenda10,  davi10, larissa10, super_davi10, super_larissa10]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - 10 niches')
#plt.figure(figsize=)
plt.savefig('ant_10_50.png')
#plt.show()
