import matplotlib.pyplot as plt

brenda = [-3.97  , 1383.64, 876.14 , 806.64 , 12.00  , 41.79  , 71.94  , 922.53 , 587.43 , 947.58 ]
davi = [959.29 , 402.03 , 24.88  , 934.61 , 23.99  , 30.69  , 200.19 , 1303.07, 751.27 , 883.58 ]
larissa = [293.90 , 1214.84, 534.91 , 638.72 , 1752.58, 23.67  , 1062.83, 1055.44, 1288.65, 1109.48]
super_davi = [1504.18, 400.26 , 1465.00, 1034.55, 1797.58, 946.51 , 899.04 , 1618.91, 1797.89, 1737.46]
super_larissa = [1494.09, 956.88 , 1636.86, 1336.67, 1199.77, 926.09 , 1160.42, 1558.24, 1280.56, 2256.17, 1680.66]

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - 2 niches')
#plt.figure(figsize=)
plt.savefig('ant_2_50.png')
#plt.show()
