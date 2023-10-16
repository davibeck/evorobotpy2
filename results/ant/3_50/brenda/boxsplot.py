import matplotlib.pyplot as plt

episode_1 = [-3.97, 1383.64, 876.14, 806.64, 12.00, 41.79, 71.94, 922.53, 587.43, 947.58]
episode_5 = []
episode_10 = []
la_es = [2049.02 ,1989.27 ,1761.93 ,2314.13 ,1956.24 ,942.76  ,2253.62 ,1627.53 ,2072.80 ,1792.51]

data = [episode_1, episode_5, episode_10, la_es]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['1 Episode', '5 Episodes', '10 Episodes', 'LA-Es'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - OpenAi-Es-Ne - 1 x 5 x 10')
#plt.figure(figsize=)
plt.savefig('ant_brenda_1_5_10.png')
#plt.show()
