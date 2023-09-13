import matplotlib.pyplot as plt

brenda5 = [751.08 , 820.54 , -7.93  , 48.70  , 3.97   , 875.85 , 1264.78, 55.18  , 1085.41, 315.30 ]
davi5 = [65.63  , 34.13  , 1143.82, 381.57 , 1220.91, 1237.89, 1126.28, 475.03 , 352.81 , 1360.22]
larissa5 = [1042.23, 986.44 , 1463.42, 788.16 , 866.81 , 1501.53, 64.26  , 983.56 , 1164.84, 985.55 ]
super_davi5 = [1300.20, 1659.51, 1666.34, 1246.22, 1705.65, 1255.89, 684.52 , 982.67 , 1556.87, 1410.08]
super_larissa5 = [1891.03, 2169.31, 2091.71, 1827.65, 1878.88, 2181.62, 2329.85, 1426.50, 1999.50, 1645.97]

data = [brenda5,  davi5, larissa5, super_davi5, super_larissa5]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - 5 niches')
#plt.figure(figsize=)
plt.savefig('ant_5_50.png')
#plt.show()
