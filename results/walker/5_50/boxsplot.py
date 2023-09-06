import matplotlib.pyplot as plt

brenda = [120.44, 105.92, 424.59, 784.00, 692.93, 12.19 , 73.15 , 275.48, 168.76, 460.39]
davi = [12.01 , 72.93 , 106.26, 439.61, 787.42, 12.31 , 11.12 , 90.06 , 299.08, 287.48]
larissa = [14.58  , 172.29 , 576.46 , 1385.97, 299.27 , 1443.33, 1133.08, 456.65 , 634.15 , 757.37 ]
super_davi = [789.16 , 660.36 , 83.25, 512.67 , 971.75 , 1412.65, 856.36 , 438.62 , 659.33 , 676.94 ]
super_larissa = [11.82  , 1179.68, 755.75 , 1409.34, 1410.98, 787.56 , 861.88 , 1581.81, 1263.18, 1590.91]

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Walker - 5 niches')
#plt.figure(figsize=)
plt.savefig('walker_5_50.png')
#plt.show()
