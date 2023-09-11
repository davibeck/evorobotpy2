import matplotlib.pyplot as plt

davi = [88.41, 92.14, 64.98, 72.99, 96.03, 93.52, 94.96, 93.24, 97.56, 119.04]
brenda = [96.36, 87.22, 86.60, 115.89, 132.55, 83.72, 128.33, 131.10, 112.52, 165.73]
larissa = [86.41, 91.30, 93.29, 80.11, 87.66, 107.37, 93.09, 86.08, 98.98, 87.12]
super_davi = [111.54, 87.06, 128.25, 129.47, 129.02, 145.42, 83.96, 107.25, 152.84, 152.97]
super_larissa = [84.80, 99.95, 96.90, 94.56, 84.46, 83.54, 103.03, 90.37, 89.42, 102.20]


data = [brenda, davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Humanoid - 3 niches')
#plt.figure(figsize=)
plt.savefig('humanoid_3_50.png')
