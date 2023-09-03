import matplotlib.pyplot as plt

brenda = [1578.34, 1295.90, -13.59 , 1789.39, 1213.57, 2055.60, 2146.55, 1198.11, 1117.14, 1405.39]
davi = [1163.76, 1132.11, 930.49 , 2240.85, 1618.00, 1878.97, 1841.37, 1609.50, 960.43 , 1058.69]
larissa = [1268.97, 1885.22, 236.86 , 2062.58, 1893.48, 1531.03, 1567.79, 1667.87, 1990.61, 233.72 ]
super_davi = [1263.52, 1499.21, 1918.60, 2004.17, 1876.71, 1787.56, 2094.18, 2161.57, 1162.04, 1717.05]
super_larissa = [1427.37, 1553.29, 1979.35, 1589.56, 1995.10, 2164.77, 1074.79, 1870.94, 1907.50, 1967.66]

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Hopper - 3 niches')
#plt.figure(figsize=)
plt.savefig('hopper_3_50.png')
#plt.show()
