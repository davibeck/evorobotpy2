import matplotlib.pyplot as plt

brenda = [168.22, 122.52, 145.40, 132.72, 162.39, 111.62, 83.33, 111.85, 135.91, 115.34]
davi = [107.76, 88.20, 134.25, 157.70, 125.61, 93.16, 79.63, 103.18, 99.95, 125.09]
larissa = [97.39, 99.67, 95.52, 92.19, 114.19, 83.08, 96.99, 67.15, 84.74, 93.24, 92.33]
super_davi = [93.09, 91.96, 138.22, 126.53, 153.72, 95.95, 86.53, 117.71, 123.76, 105.97]
super_larissa = [78.57, 82.96, 95.41, 91.06, 74.86, 79.93, 88.43, 77.61, 88.09, 105.19]


data = [brenda, davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Humanoid - 5 niches')
#plt.figure(figsize=)
plt.savefig('humanoid_5_50.png')
