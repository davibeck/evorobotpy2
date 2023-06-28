import matplotlib.pyplot as plt

davi_3n_50g = [2626.66, 2122.09, 2185.25, 639.55, 1819.46, 1991.76, 1619.81, 2616.79, 2282.71, 1537.18]
brenda_3n_50g = [2307.02, 15.11, 14.67, 844.06, 1935.48, 1909.44, 1243.27, 2336.71, 2437.67, 1644.63]
larissa_333 = [1558.69, 2323.05, 2665.83, 1912.86, 2647.51, 1607.58, 1052.73, 1231.22, 1001.41, 1861.34]
same_seed_3_50 = [2636.60, 1712.71, 1852.64, 2278.32, 2057.86, 1661.50, 1459.21, 1096.77, 959.53 , 841.84]


data = [davi_3n_50g,  brenda_3n_50g, larissa_333, same_seed_3_50]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['Davi 3-50', 'Brenda 3-50', 'Larissa 333', 'SS 3-50'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - OpenAi-Es vs OpenAi-Es-Ne')
#plt.figure(figsize=)
#plt.savefig('teste.png')
plt.show()
