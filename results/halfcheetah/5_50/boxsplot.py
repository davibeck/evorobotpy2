import matplotlib.pyplot as plt

davi_5n_50g = [2096.79, 1882.49, 1708.87, 1761.49, 16.46, 1542.16, 1407.60, 2253.80, 2245.84, 1437.40]
brenda_5n_50g = [1286.96, 1605.22, 1599.83, 1356.35, 2239.50, 1281.39, 1762.46, 590.17, 2017.05, 1247.02]
larissa_500 = [1895.62, 2216.35, 676.84 , 2202.48, 1909.15, 916.04 , 1490.30, 1998.81, 2636.05, 2320.15]
#ss_5_50 = [2581.93,1533.86,1631.43,1841.13,1091.57,463.12 ,2079.90,461.91 ,115.37 ,1539.69]


data = [davi_5n_50g,  brenda_5n_50g, larissa_500]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['Davi 5-50', 'Brenda 5-50', 'Larissa 500'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - OpenAi-Es vs OpenAi-Es-Ne')
#plt.figure(figsize=)
plt.savefig('5_50.png')
#plt.show()
