import matplotlib.pyplot as plt

one_episode = [1163.76, 1132.11, 930.49 , 2240.85, 1618.00, 1878.97, 1841.37, 1609.50, 960.43 , 1058.69]
five_episodes = [1696.09, 2014.77, 2143.36, 2013.19, 1506.54, 1648.72, 1968.14, 1781.34, 2349.49, 1924.12]
ten_episodes = [1936.20, 2209.71, 1795.31, 2310.07, 2208.95, 2265.03, 1256.07, 1466.56, 1704.81, 270.24]

data = [one_episode,  five_episodes, ten_episodes]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['1 Episode', '5 Episodes', '10 Episodes'])
ax.set_ylabel('Valores Fitness')

plt.title('Hopper - DB-Es - 1 x 5 x 10 Episodes')
#plt.figure(figsize=)
plt.savefig('hopper_1_5_10.png')
#plt.show()
