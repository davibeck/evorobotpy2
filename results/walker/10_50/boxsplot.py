import matplotlib.pyplot as plt

brenda = [10.63 , 92.26 , 268.29, 91.36 , 102.00, 172.82, 102.04, 11.08 , 465.51, 103.24]
davi = [134.69, 82.09 , 397.70, 325.77, 140.38, 314.99, 135.86, 383.11, 103.04, 555.45]
larissa = [232.45 ,1119.44,512.75 ,106.27 ,105.27 ,463.79 ,1118.21, 767.63 ,1202.95]
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
