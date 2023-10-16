import matplotlib.pyplot as plt

episode_1 = [959.29, 402.03, 24.88, 934.61, 23.99, 30.69, 200.19, 1303.07, 751.27, 883.58]
episode_5 = [1626.74, 1637.87, 1104.87, 1411.43, 1486.22, 240.64, 1722.92, 1469.98, 1339.69, 619.05]
episode_10 = [53.21, 2069.03, 1376.71, 1068.42, 1460.41, 944.82, 1028.23, 1455.17, 1691.06, 941.87]
la_es = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]

data = [episode_1, episode_5, episode_10, la_es]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['1 Episode', '5 Episodes', '10 Episodes', 'LA-Es'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - FixedSeed-NE - 1 x 5 x 10')
#plt.figure(figsize=)
plt.savefig('ant_fixedseed_1_5_10.png')
#plt.show()
