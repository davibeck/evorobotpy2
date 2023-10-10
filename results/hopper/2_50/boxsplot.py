import matplotlib.pyplot as plt

brenda = [24.84  , 1281.87, 1192.89, 1588.59, 1523.10, 834.65 , 1425.22, 971.58 , 1938.87, 1545.74]
davi = [1099.09, 1515.24, 1726.76, 1514.44, 1387.73, 1907.77, 1454.61, 1441.08, 16.06  , 1723.47]
larissa = [1119.49, 1300.68, 2000.04, 1385.62, 1965.39, 1275.55, 27.38  , 940.57 , 1824.46, 2123.31]
random_davi = [1574.62, 1522.07, 1906.55, 1698.16, 2092.44, 1349.22, 1441.61, 1721.40, 1620.04, 1775.66]
super_davi = [1309.40, 1711.05, 1147.97, 1062.49, 1415.73, 1509.84, 3.97   , 1438.10, 2067.40, 1979.26]
super_larissa = [1311.60, 1339.94, 1525.89, 1794.36, 1528.63, 1721.22, 1823.29, 2009.18, 1831.85, 1693.03]

data = [brenda,  davi, random_davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES','RDB-Es', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Hopper - 2 Niches')
#plt.figure(figsize=)
#plt.savefig('hopper_2_50.png')
plt.show()
