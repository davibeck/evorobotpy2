import matplotlib.pyplot as plt

davi_10n_50g = [1803.83, 1527.64, 14.73 , 1567.81, 2040.28, 84.69 , 1592.13, 16.85 , 1592.79, 1107.09]
brenda_10n_50g = [12.06,  291.76 ,42.37  ,761.07 ,14.58  ,770.81 ,1944.82,1890.16,1257.22,1564.35]
larissa_100 = [840.33, 2555.51, 2274.35, 1252.90, 2191.86, 1735.66, 2871.30, 2830.40, 2233.00, 2540.72]


data = [davi_10n_50g,  brenda_10n_50g, larissa_100]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['DB-Es', 'OpenAi-Es-Ne', 'LA-Es'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - 10 niches')
#plt.figure(figsize=)
plt.savefig('10_50.png')
#plt.show()
