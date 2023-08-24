import matplotlib.pyplot as plt

davi_5n_50g = [2096.79, 1882.49, 1708.87, 1761.49, 16.46, 1542.16, 1407.60, 2253.80, 2245.84, 1437.40]
brenda_5n_50g = [1286.96, 1605.22, 1599.83, 1356.35, 2239.50, 1281.39, 1762.46, 590.17, 2017.05, 1247.02]
larissa_500 = [1895.62, 2216.35, 676.84 , 2202.48, 1909.15, 916.04 , 1490.30, 1998.81, 2636.05, 2320.15]
#ss_5_50 = [2581.93,1533.86,1631.43,1841.13,1091.57,463.12 ,2079.90,461.91 ,115.37 ,1539.69]
super_5n_50g = [2722.44, 2439.23, 2517.59, 1783.99, 2201.03, 2437.00, 1721.58, 2319.28, 2423.41, 2149.12]
#super_larissa = [2683.01, 2992.44, 2947.73, 2777.17, 1673.23, 2757.99, 2907.45, 1840.87, 2554.32, 2854.33]


data = [davi_5n_50g,  brenda_5n_50g, larissa_500, super_5n_50g, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['DB-Es', 'OpenAi-Es-Ne', 'LA-Es', 'DB-Es-SB', 'LA-Es-SB'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - 5 niches')
#plt.figure(figsize=)
plt.savefig('5_50_budget.png')
#plt.show()
