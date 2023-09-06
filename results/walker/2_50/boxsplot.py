import matplotlib.pyplot as plt

brenda = [284.92, 94.55 , 523.27, 508.98, 70.91 , 55.09 , 106.83, 209.38, 83.13 , 310.64]
davi = [111.59, 119.59, 390.45, 920.62, 422.62, 12.20 , 26.41 , 75.05 , 180.49, 478.04]
larissa = [118.79 ,620.39 ,589.44 ,1177.23,122.24 ,112.89 ,254.57 ,112.73 ,402.21 ,1365.03]
super_davi = [108.99 , 1122.09, 681.37 , 782.30 , 1140.09, 12.34  , 598.31 , 364.65 , 679.76 , 1175.42]
super_larissa = [14.37  , 364.13 , 520.61 , 512.21 , 1500.18, 435.07 , 619.68 , 370.00 , 1580.70, 1752.64]

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Walker - 2 niches')
#plt.figure(figsize=)
plt.savefig('walker_2_50.png')
#plt.show()
