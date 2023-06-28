import matplotlib.pyplot as plt

davi_3n_50g = [2626.66, 2122.09, 2185.25, 639.55, 1819.46, 1991.76, 1619.81, 2616.79, 2282.71, 1537.18]
davi_5n_50g = [2096.79, 1882.49, 1708.87, 1761.49, 16.46, 1542.16, 1407.60, 2253.80, 2245.84, 1437.40]
brenda_5n_50g = [1286.96, 1605.22, 1599.83, 1356.35, 2239.50, 1281.39, 1762.46, 590.17, 2017.05, 1247.02]
brenda_3n_50g = [2307.02, 15.11, 14.67, 844.06, 1935.48, 1909.44, 1243.27, 2336.71, 2437.67, 1644.63]


data = [davi_3n_50g,  brenda_3n_50g, davi_5n_50g, brenda_5n_50g]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['Davi 3-50', 'Brenda 3-50', 'Davi 5-50', 'Brenda 5-50'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - OpenAi-Es vs OpenAi-Es-Ne')
#plt.figure(figsize=)
#plt.savefig('teste.png')
plt.show()
