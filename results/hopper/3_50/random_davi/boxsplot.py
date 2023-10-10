import matplotlib.pyplot as plt

one_episode = [1346.35, 1363.48, 1735.80, 1880.34, 1722.69, 1144.52, 1625.03, 2113.52, 1360.63, 1037.83]
five_episodes = [1834.92, 1895.39, 1552.28, 2280.14, 282.41, 1952.96, 1378.68, 1581.16, 2007.77, 2025.18]
ten_episodes = [2098.58, 1914.03, 1933.59, 1873.87, 1958.35, 2157.15, 2145.63, 2246.12, 2044.28, 2084.30]

data = [one_episode,  five_episodes, ten_episodes]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['1 Episode', '5 Episodes', '10 Episodes'])
ax.set_ylabel('Valores Fitness')

plt.title('Hopper - DBR-Es - 1 x 5 x 10 Episodes')
#plt.figure(figsize=)
plt.savefig('hopper_1_5_10.png')
#plt.show()
