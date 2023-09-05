import matplotlib.pyplot as plt

brenda = [1063.09, 1173.03, 1190.32, 1285.13, 912.61 , 1058.03, 967.19 , 1369.74, 1327.43, 1456.71]
davi = [1301.21, 1374.82, 1257.51, 1099.81, 1751.52, 1408.33, 383.46 , 1103.43, 1367.56, 1380.36]
random_davi = [850.73 , 1567.06, 1370.19, 938.00 , 1378.25, 1009.34, 1084.27, 1639.83, 380.33 , 1171.17]
larissa = [1691.02, 1953.19, 1652.34, 1627.58, 1618.62, 1815.49, 1999.38, 1859.27, 2047.88, 2109.81]
super_davi = [1509.52, 1649.77, 1975.61, 1765.82, 1662.44, 1492.95, 1811.15, 1963.10, 2010.98, 2319.25]
super_larissa = [1687.19, 1865.10, 2001.02, 2051.33, 1913.84, 1373.45, 1903.17, 2123.76, 1837.16, 2139.66]

data = [brenda,  davi,random_davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES','Random', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Hopper - 10 niches')
#plt.figure(figsize=)
plt.savefig('hoppper2_10_50.png')
#plt.show()
