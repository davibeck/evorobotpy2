import matplotlib.pyplot as plt

davi = [77.46, 93.48, 96.05, 89.34, 147.01, 89.90, 90.36, 78.90, 163.99, 83.42]
brenda = [126.23, 108.51, 137.61, 124.77, 154.05, 96.18 , 94.60 , 82.88 , 109.12, 150.39]
larissa = [100.03, 86.54, 110.25, 99.75, 79.76, 103.34, 82.82, 93.66, 111.67, 99.00]
super_davi = [109.45, 91.32, 105.44, 91.58, 157.61, 93.97, 148.25, 68.43, 94.94, 139.68]
super_larissa = [105.24, 96.00, 125.61, 104.93, 84.16, 87.92, 82.53, 83.78, 102.25, 83.78, 103.41]


data = [brenda, davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Humanoid - 2 niches')
#plt.figure(figsize=)
plt.savefig('humanoid_2_50.png')
