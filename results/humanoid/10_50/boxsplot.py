import matplotlib.pyplot as plt

brenda = [116.69, 113.75, 116.18, 132.42, 132.85, 124.11, 108.69, 118.28, 127.42, 170.18]
davi = [123.39, 193.10, 125.09, 163.31, 146.97, 125.62, 126.27, 129.18, 119.51, 153.67]
larissa = [65.95, 64.92, 73.95, 80.90, 78.50, 114.25, 74.55, 79.96, 85.58, 79.67]
super_davi = [99.18, 114.86, 118.14, 98.91, 146.47, 124.34, 129.81, 128.04, 107.57, 103.63]
super_larissa = [115.23, 108.48, 118.78, 105.96, 89.56, 92.35, 105.24, 85.52, 104.39, 96.71]


data = [brenda, davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Humanoid - 10 niches')
#plt.figure(figsize=)
plt.savefig('humanoid_10_50.png')
