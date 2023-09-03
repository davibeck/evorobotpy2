import matplotlib.pyplot as plt

brenda = [1235.89, 1450.44, 1350.04, 1542.17, 1169.90, 1438.30, 1185.31, 1446.52, 2131.47, 1219.80]
davi = [897.15 , 714.81 , 1292.23, 1446.27, 661.58 , 17.92  , 57.24  , -2.33  , 923.54 , 1136.67]
larissa = [1662.42, 1676.18, 1343.32, 1867.76, 1729.07, 1884.13, 1413.59, 1649.83, 2150.13, 1750.52]
super_davi = [1669.24, 1487.05, 1962.90, 2203.44, 1481.63, 1560.19, 1459.67, 1717.82, 2033.88, 1492.93]
super_larissa = [1839.70, 1472.02, 1610.30, 2522.95, 1511.00, 1589.31, 1830.36, 1447.09, 1739.53, 2111.75]

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Hopper - 5 niches')
#plt.figure(figsize=)
plt.savefig('hopper_5_50.png')
#plt.show()
