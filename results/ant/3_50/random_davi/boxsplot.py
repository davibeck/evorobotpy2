import matplotlib.pyplot as plt

episode_1 = [811.61, 1331.04, 416.88, 1115.72, 1615.40, 708.64, 479.88, 1366.88, 1188.54, 1337.45]
episode_5 = [995.87, 1584.00, 1246.12, 1495.55, 942.67, 1296.84, 1310.79, 1200.12, 620.41, 1101.23]
episode_10 = [1575.84, 1435.35, 1750.31, 1621.40, 776.93, 1539.64, 1231.47, 1714.27, 1401.24, 1563.00]
la_es = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]

data = [episode_1, episode_5, episode_10, la_es]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['1 Episode', '5 Episodes', '10 Episodes', 'LA-Es'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - RandSeed-NE - 1 x 5 x 10')
#plt.figure(figsize=)
plt.savefig('ant_randseed_1_5_10.png')
#plt.show()
