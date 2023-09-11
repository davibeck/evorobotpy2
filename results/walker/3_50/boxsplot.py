import matplotlib.pyplot as plt

brenda = [12.80 , 11.98 , 74.62 , 471.60, 237.86, 104.35, 372.94, 196.51, 169.33, 324.70]
davi = [12.60  , 83.13  , 88.45  , 703.30 , 435.81 , 82.70  , 447.04 , 1228.85, 610.88 , 869.95 ]
random_davi = [12.46  , 888.82 , 1265.24, 505.56 , 825.87 , 720.00 , 526.47 , 1072.33, 1468.38, 1531.24]
larissa = [718.81 , 614.22 , 920.25 , 848.58 , 588.62 , 160.63 , 1373.55, 199.94 , 854.87 , 870.88 ]
super_davi = [1210.80, 973.53 , 12.50  , 58.66  , 12.19  , 309.14 , 1002.83, 1443.90, 127.00 , 416.87 ]
super_larissa = [741.34 , 668.10 , 588.62 , 1369.87, 1642.38, 727.13 , 270.20 , 644.54 , 648.38 , 608.35 ]

data = [brenda,  davi,random_davi,  larissa, super_davi, super_larissa]

fig, ax = plt.subplots()
ax.boxplot(data)

ax.set_xticklabels(['OpenAi-ES-NE', 'DB-ES', 'Random', 'LA-ES', 'DB-SP', 'LA-SP'])
ax.set_ylabel('Valores Fitness')

plt.title('Boxplot - Walker - 3 niches')
#plt.figure(figsize=)
plt.savefig('walker_3_50.png')
#plt.show()
