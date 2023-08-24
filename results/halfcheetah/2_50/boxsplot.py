import matplotlib.pyplot as plt

davi_2n_50g = [2232.16, 1471.19, 2508.74, 1381.31, 2662.64, 15.91  ,351.30 , 2249.77, 2655.73, 944.21]
brenda_2n_50g = [1692.05, 356.32 , 1288.87, 840.49 , 1753.54, 2204.37, 1300.69, 624.32 , 1392.67, 1085.66]
larissa_500 = [1982.69, 2235.67, 2333.56, 2524.10, 684.58 , 1561.83, 1975.81, 1664.63, 1221.70, 392.11 ]
super_2n_50g = [1717.53, 1549.67, 1402.20, 2412.98, 1785.64, 2321.78, 2095.40, 22.52  , 2062.77, 2806.13]


data = [davi_2n_50g,  brenda_2n_50g, larissa_500]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['DB-Es', 'OpenAi-Es-Ne', 'LA-Es'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - 2 niches')
#plt.figure(figsize=)
plt.savefig('2_50.png')
#plt.show()
