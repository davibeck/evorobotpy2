import matplotlib.pyplot as plt

brenda = [569.79 , 967.32 , 73.61  , 13.81  , 1078.41, 745.15 , 916.23 , 5.91 , 1010.00, 301.26 ]
davi = [897.15 , 714.81 , 1292.23, 1446.27, 661.58 , 17.92  , 57.24  , -2.33  , 923.54 , 1136.67]
random_davi = [706.64 , 1476.61, 702.85 , 1251.74, 441.51 , 10.39  , 75.43  , 1108.53, 724.01 , 1006.32]
larissa = [802.03 , 459.78 , 832.09 , 993.79 , 1099.31, 1544.66, 1053.97, 676.16 , 30.99  , 1222.83]
super_davi = [1075.94, 299.93 , 905.49 , 1211.24, -43.59 , 992.92 , 1197.40, 562.78 , 1239.50, 1323.91]
super_larissa = [1668.10, 877.70 , 1409.08, 623.21 , 1467.29, 745.22 , 981.61 , 1473.59, 991.49 , 792.80 ]

data = [brenda,  davi, random_davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'Random', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - 2 niches')
#plt.figure(figsize=)
plt.savefig('ant_2_50.png')
#plt.show()
