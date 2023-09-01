import matplotlib.pyplot as plt

brenda = []
davi = []
larissa = []
super_davi = []
super_larissa = []

data = [brenda,  davi, larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Ant - 2 niches')
#plt.figure(figsize=)
plt.savefig('ant_2_50.png')
#plt.show()
